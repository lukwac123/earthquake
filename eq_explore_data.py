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