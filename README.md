# Pobieranie i przetwarzanie danych w formacie GeoJSON.

Pobieranie danych w formacie GeoJSON z użyciem biblioteki **json** oraz utworzenie mapy świata przy pomocy modułu **plotly.express**
wraz z przedstawieniem miejsc występowania trzęsień ziemi i ich siły.

W pierwszej kolejności importujemy plik w formacie _*.geojson_, z którego pobierzemy potrzebne informacje takie jak długość i szerokość geograficzna 
oraz siła trzęsieniai. Robimy to używając funkcji **json.loads()** przy pomocy której przekształcamy plik do bardziej zrozumiałej i czytelnej formy.
Kolejnym etapem jest wyodrębnienie danych z informacją o sile trzęsienia i miejscu występowania. Następnie wykorzystując funkcję **scatter_geo()** tworzymy mapę świata 
i umieszczamy na niej punkty trzęsień ziemi. Dostosowanie mapy wykonujemy w dodając parametry w wywołaniu tej funkcji. Rysunek 1. przedstawia gotowy efekt prac.

![earthquake](https://github.com/user-attachments/assets/e1b22aca-d01f-4d84-a07e-a49dd839a443)

<sup>Rysunek 1. Interaktywna mapa trzęsień ziemi na świecie.
