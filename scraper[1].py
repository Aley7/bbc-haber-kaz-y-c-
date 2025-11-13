import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://www.bbc.com/turkce"
response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h3")

data = []
for h in headlines:
    title = h.get_text(strip=True)
    if title:
        data.append({
            "Başlık": title,
            "Kaynak": "BBC Türkçe",
            "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

df = pd.DataFrame(data)
df.to_csv("haber_basliklari.csv", index=False, encoding="utf-8-sig")
print(f"✅ Toplam {len(df)} haber başlığı kaydedildi.")
