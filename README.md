# Weather Data Scraper

This Python script allows you to scrape weekly weather data for 81 provinces in Turkey/Türkiye from the website [havadurumux.net](https://www.havadurumux.net/). The scraped data includes the date (Date), highest temperature (Up), and lowest temperature (Low) for each day of the week.

## Requirements
- Python 3.x
- Requests
- Pandas
- BeautifulSoup

You can install the required packages using the following command:
```bash
pip install requests pandas beautifulsoup4
```

## Usage
1. Clone this repository or download the script [app.py](app.py).
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:
   ```bash
   python app.py
   ```
4. The script will scrape the weather data for the specified provinces and save it to a CSV file named `weekly_weather_data.csv`.

## Provinces
The script is set up to scrape weather data for the following provinces in Turkey/Türkiye:
- Adana
- Adiyaman
- Afyonkarahisar
- Agri
- Amasya
- Ankara
- Antalya
- Artvin
- Aydin
- Balikesir
- Bilecik
- Bingol
- Bitlis
- Bolu
- Burdur
- Bursa
- Canakkale
- Cankiri
- Corum
- Denizli
- Diyarbakir
- Duzce
- Edirne
- Elazig
- Erzincan
- Erzurum
- Eskisehir
- Gaziantep
- Giresun
- Gumushane
- Hakkari
- Hatay
- Igdir
- Isparta
- Istanbul
- Izmir
- Kahramanmaras
- Karabuk
- Karaman
- Kars
- Kastamonu
- Kayseri
- Kirikkale
- Kirklareli
- Kirsehir
- Kilis
- Kocaeli
- Konya
- Kutahya
- Malatya
- Manisa
- Mardin
- Mersin
- Mugla
- Mus
- Nevsehir
- Nigde
- Ordu
- Osmaniye
- Rize
- Sakarya
- Samsun
- Siirt
- Sinop
- Sivas
- Sanliurfa
- Sirnak
- Tekirdag
- Tokat
- Trabzon
- Tunceli
- Usak
- Van
- Yalova
- Yozgat
- Zonguldak

## Output
The scraped weather data is saved as a CSV file named `weekly_weather_data.csv`. The file is encoded in UTF-8 with a BOM signature (`utf-8-sig`) to ensure proper encoding compatibility.

## Author

Doğan Seyfi Şen

Note: This script is intended for educational purposes, and it is crucial to review and respect the terms of service of the website from which data is being scraped. Always be mindful of not violating any terms or policies.
