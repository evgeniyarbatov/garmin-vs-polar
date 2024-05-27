CREATE EXTENSION IF NOT EXISTS postgis;

CREATE OR REPLACE FUNCTION import_route_from_csv(csv_file_path TEXT, target_table TEXT)
RETURNS VOID AS $$
BEGIN
    -- Ensure the target table exists, creating it if necessary
    EXECUTE FORMAT('
        CREATE TABLE IF NOT EXISTS %I (
            id SERIAL PRIMARY KEY,
            time TIMESTAMPTZ,
            location GEOMETRY(Point, 4326)
        )', target_table);

    -- Create a temporary table
    CREATE TEMP TABLE tmp_route (
        id SERIAL PRIMARY KEY,
        time TIMESTAMPTZ,
        latitude DECIMAL,
        longitude DECIMAL
    );

    -- Copy data from the CSV file to the temporary table
    EXECUTE FORMAT('COPY tmp_route (time, latitude, longitude) FROM %L DELIMITER '','' CSV HEADER', csv_file_path);

    -- Insert data from the temporary table into the target table
    EXECUTE FORMAT('
        INSERT INTO %I (time, location)
        SELECT time, ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)
        FROM tmp_route', target_table);

    -- Drop the temporary table
    DROP TABLE tmp_route;
END;
$$ LANGUAGE plpgsql;

SELECT import_route_from_csv('/data/route.csv', 'gpx_route');
SELECT import_route_from_csv('/data/polar.csv', 'polar_route');
SELECT import_route_from_csv('/data/garmin.csv', 'garmin_route');