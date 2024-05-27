# Scripts

Analyze running data recorded by Garmin and Polar.

## Setup

```
python3 -m venv ~/.venv/garmin-vs-polar
source ~/.venv/garmin-vs-polar/bin/activate
pip install -r requirements.txt
```

## Create plots

Location, elevation and distance plots:

```
python plots.py \
../data/27-05-2023 \
../metadata/27-05-2023
```

## Import to PostGIS

```
python postgis-import.py \
../data/27-05-2023 \
../postgis/data/
```