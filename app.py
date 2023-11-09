import requests
import pandas as pd
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def scrape_weather_data(province):
    url = f"https://www.havadurumux.net/{province}-hava-durumu/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")

    weather_data = []

    for row in soup.find("tbody").find_all("tr")[:7]: # A week
        col = row.find_all("td")
        Date = col[0].text
        Date_Parts = Date.split(",") 
        Date = Date_Parts[0].strip()
        Up = extract_float(col[2].text)
        Low = extract_float(col[3].text)

        weather_data.append({"Date": Date, "Up": Up, "Low": Low})

    return weather_data

def extract_float(text):
    # Convert text to float type
    result = ''.join(c for c in text if c.isdigit() or c in '.-')
    return float(result) if result else None

provinces = [
    "Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Amasya", "Ankara", "Antalya", "Artvin", "Aydin", "Balikesir",
    "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli",
    "Diyarbakir", "Duzce", "Edirne", "Elazig", "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun",
    "Gumushane", "Hakkari", "Hatay", "Igdir", "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman",
    "Kars", "Kastamonu", "Kayseri", "Kirikkale", "Kirklareli", "Kirsehir", "Kilis", "Kocaeli", "Konya", "Kutahya",
    "Malatya", "Manisa", "Mardin", "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize",
    "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Sanliurfa", "Sirnak", "Tekirdag", "Tokat", "Trabzon", "Tunceli",
    "Usak", "Van", "Yalova", "Yozgat", "Zonguldak"
]

all_weather_data = []

for province in provinces:
    weather_data = scrape_weather_data(province)

    for data in weather_data:
        data["Province"] = province
        all_weather_data.append(data)

all_weather_df = pd.DataFrame(all_weather_data)
# Save as .csv file
all_weather_df.to_csv("weekly_weather_data.csv", index=False, encoding='utf-8-sig')
