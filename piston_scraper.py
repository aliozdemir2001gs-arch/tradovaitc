import requests
from bs4 import BeautifulSoup

url = "https://www.gelbeseiten.de/Suche/piston/Händler/Konstanz"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

firmalar = soup.find_all("article")
print(f"Bulunan article sayısı: {len(firmalar)}")
