# Garmin vs Polar

Compare recordings from Garmin and Polar with the actual route.

Write up of findings: https://medium.com/@arbatov/two-views-of-one-run-10739b78b4e6

## Metrics

These are the metrics I use for comparison:

- location
- elevation 
- distance

## Structure

Main:

- `data`: raw GPX files from Garmin Explore and Polar Flow
- `metadata`: metadata about the run based on the raw data
- `scripts`: scripts which take the raw data and generate metadata

Extras:

- `explore`: experimental scripts and notebooks
- `manuals`: user manuals for each device

## Hardware

- [Garmin eTrex Solar](https://www.garmin.com.sg/products/outdoor/etrex-solar/) (Nov 16, 2023)
- [Polar Vantage V](https://support.polar.com/e_manuals/vantage-v/polar-vantage-v-user-manual-english/content/introduction.htm) (Sept 13, 2018)
