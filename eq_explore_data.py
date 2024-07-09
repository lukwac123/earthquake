from pathlib import Path
import json

# Odczytanie danych jako ciągu tekstowego i ich konwersja na obiekt Pythona.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Utworzenie znacznie czytelniejszej wersji pliku danych.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Analiza wszystkich trzęsień na podstawie zbioru danych.
all_eq_data = all_eq_data['features']
# Poniższy wiersz wyświetla liczbę trzęsień ziemi.
# print(len(all_eq_data))

mags, lons, lats = [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])