import gpxpy
import sys

import pandas as pd
import matplotlib.pyplot as plt

def parse_gpx(filepath):
  gpx_file = open(filepath, 'r')
  gpx = gpxpy.parse(gpx_file)

  data = []
  for track in gpx.tracks:
    for segment in track.segments:
      for point in segment.points:
        data.append({
          'time': point.time,
          'latitude': point.latitude, 
          'longitude': point.longitude,
          'elevation': point.elevation,
        })

  df = pd.DataFrame(data)
  df['time'] = df['time'].dt.tz_localize(None)
  
  return df

def main(args):
  input_dir = args[0]
  output_dir = args[1]

if __name__ == "__main__":
    main(sys.argv[1:])