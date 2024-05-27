import gpxpy
import sys
import os
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx
import matplotlib.dates as mdates

from pytz import timezone
from geopy.distance import geodesic

matplotlib.rcParams['timezone'] = 'Asia/Singapore'

def parse_gpx(filepath):
  gpx_file = open(filepath, 'r')
  gpx = gpxpy.parse(gpx_file)

  data = []
  distance = 0
  prev_lat, prev_lng = None, None

  for track in gpx.tracks:
    for segment in track.segments:
      for point in segment.points:
        lat, lng = point.latitude, point.longitude,

        time = point.time.astimezone(timezone('Asia/Singapore')) if point.time else None

        if prev_lat != None and prev_lng != None:
          distance += geodesic((prev_lat, prev_lng), (lat, lng)).meters / 1000.0

        data.append({
          'time': time,
          'latitude': lat, 
          'longitude': lng,
          'elevation': point.elevation,
          'distance': distance,
        })

        prev_lat, prev_lng = lat, lng

  df = pd.DataFrame(data)
  
  return df

def main(args):
  input_dir = args[0]
  output_dir = args[1]

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  garmin_df = parse_gpx(input_dir + '/garmin.gpx')
  polar_df = parse_gpx(input_dir + '/polar.gpx')
  route_df = parse_gpx(input_dir + '/route.gpx')
  elevation_df = parse_gpx(input_dir + '/elevation.gpx')

  plt.figure(figsize=(15, 8))
  plt.plot(polar_df['longitude'], polar_df['latitude'], color='blue', label='Polar')
  plt.plot(garmin_df['longitude'], garmin_df['latitude'], color='red', label='Garmin')
  plt.plot(route_df['longitude'], route_df['latitude'], color='black', label='Route')
  ctx.add_basemap(plt.gca(), crs='EPSG:4326', source=ctx.providers.OpenStreetMap.Mapnik)
  plt.legend()
  plt.xticks([], [])
  plt.yticks([], [])
  plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
  plt.savefig(output_dir + '/' + 'location.png')

  plt.figure(figsize=(12, 6))
  plt.plot(polar_df['time'], polar_df['elevation'], color='blue', label='Polar')
  plt.plot(garmin_df['time'], garmin_df['elevation'], color='red', label='Garmin')
  plt.plot(elevation_df['time'], elevation_df['elevation'], color='black', label='Actual elevation')
  plt.xlabel('Time')
  plt.ylabel('Elevation (m)')
  plt.legend()
  plt.grid(True)
  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
  plt.savefig(output_dir + '/' + 'elevation.png')

if __name__ == "__main__":
    main(sys.argv[1:])