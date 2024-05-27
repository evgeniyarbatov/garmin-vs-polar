import gpxpy
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

from pytz import timezone

def parse_gpx(filepath):
  gpx_file = open(filepath, 'r')
  gpx = gpxpy.parse(gpx_file)

  data = []
  for track in gpx.tracks:
    for segment in track.segments:
      for point in segment.points:
        time = point.time.astimezone(timezone('Asia/Singapore')) if point.time else None
        data.append({
          'time': time,
          'latitude': point.latitude, 
          'longitude': point.longitude,
          'elevation': point.elevation,
        })

  df = pd.DataFrame(data)
  
  return df

def plot_location(df, route_df, label, color, output_dir, filename):
  plt.figure(figsize=(12, 6))
  plt.plot(df['longitude'], df['latitude'], color=color, linestyle='-', label=label)
  plt.plot(route_df['longitude'], route_df['latitude'], color='black', linestyle='-', label='Route')
  ctx.add_basemap(plt.gca(), crs='EPSG:4326', source=ctx.providers.OpenStreetMap.Mapnik)
  plt.xlabel('Longitude')
  plt.ylabel('Latitude')
  plt.title('Latitude and Longitude Plot')
  plt.legend()
  plt.grid(True)
  plt.savefig(output_dir + '/' + filename)

def main(args):
  input_dir = args[0]
  output_dir = args[1]

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  garmin_df = parse_gpx(input_dir + '/garmin.gpx')
  polar_df = parse_gpx(input_dir + '/polar.gpx')
  route_df = parse_gpx(input_dir + '/route.gpx')

  plot_location(polar_df, route_df, 'Polar', 'blue', output_dir, 'polar-location.png')
  plot_location(garmin_df, route_df, 'Garmin', 'red', output_dir, 'garmin-location.png')

  plt.figure(figsize=(12, 6))
  plt.plot(polar_df['time'], polar_df['elevation'], color='blue', label='Polar')
  plt.plot(garmin_df['time'], garmin_df['elevation'], color='red', label='Garmin')
  plt.xlabel('Time')
  plt.ylabel('Elevation (m)')
  plt.title('Elevation over Time')
  plt.legend()
  plt.grid(True)
  plt.savefig(output_dir + '/' + 'elevation.png')

if __name__ == "__main__":
    main(sys.argv[1:])