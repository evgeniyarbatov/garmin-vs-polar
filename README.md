# Garmin vs Polar

Compare recordings from Garmin and Polar with the actual route.

## Metrics

These are the metrics I use for comparison:

- location
- elevation 
- distance

## User guide

GPX data from Polar and Garmin:

- download Polar GPX from https://flow.polar.com/ (`polar.gpx`)
- download Garmin GPX from Garmin Explore app (`garmin.gpx`)
- correct elevation on Strava activity and download GPX from Strava (`elevation.gpx`)

GPX for the route:

- use Google Maps to get coordinates of start and stop location
- use [`get-segment.py`](https://github.com/evgeniyarbatov/gpx-utils/blob/main/get-segment.py) to extract slice of GPX route based on start/stop location
- save resulting GPX as `route.gpx`

Import data into PostGIS for analyzing location error:

- convert GPX files to CSV with [`postgis-import.py`](https://github.com/evgeniyarbatov/garmin-vs-polar/blob/main/scripts/postgis-import.py)
- start PostGIS with Docker and seed CSV file: `docker compose up --build`

## Hardware

- [Garmin eTrex Solar](https://www.garmin.com.sg/products/outdoor/etrex-solar/) (Nov 16, 2023)
- [Polar Vantage V](https://support.polar.com/e_manuals/vantage-v/polar-vantage-v-user-manual-english/content/introduction.htm) (Sept 13, 2018)

## Notes

Write up of findings: https://medium.com/@arbatov/two-views-of-one-run-10739b78b4e6
