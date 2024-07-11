from pathlib import Path
import json

import plotly.express as px

# Odczytanie danych jako ciągu tekstowego i ich konwersja na obiekt Pythona.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Analiza wszystkich trzęsień na podstawie zbioru danych.
all_eq_data = all_eq_data['features']

# Wyodrębnienie danych: siła trzęsienia oraz miejsce.
mags, lons, lats = [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = 'Trzęsienia ziemi na świecie.'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Siła'},
                     projection='natural earth',
                     )
fig.show()