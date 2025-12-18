import sys

import pandas as pd
import gpxpy


FIXED_TIMESTAMP = "2024-05-26 22:19:06+00:00"


def create_csv(gpx_filepath, csv_filepath):
    gpx_file = open(gpx_filepath, "r")
    gpx = gpxpy.parse(gpx_file)

    data = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                data.append(
                    {
                        "time": point.time if point.time else FIXED_TIMESTAMP,
                        "latitude": point.latitude,
                        "longitude": point.longitude,
                    }
                )
    df = pd.DataFrame(data)

    columns = [
        "time",
        "latitude",
        "longitude",
    ]
    df.to_csv(
        csv_filepath,
        columns=columns,
        header=False,
        index=False,
    )


def main(args):
    input_dir = args[0]
    output_dir = args[1]

    create_csv(input_dir + "/polar.gpx", output_dir + "/polar.csv")
    create_csv(input_dir + "/garmin.gpx", output_dir + "/garmin.csv")
    create_csv(input_dir + "/route.gpx", output_dir + "/route.csv")


if __name__ == "__main__":
    main(sys.argv[1:])
