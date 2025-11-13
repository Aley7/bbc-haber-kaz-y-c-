
# BBC Türkçe Haber Başlıkları Kazıyıcı

## 📌 Projenin Amacı
Python kullanarak BBC Türkçe web sitesindeki haber başlıklarını çekmek.

## ⚙️ Kullanılan Teknolojiler
- Python 3.x
- requests
- BeautifulSoup4
- pandas
- WordCloud

## 🚀 Nasıl Çalışır?
1. BBC Türkçe anasayfasına HTTP isteği gönderilir.
2. Gelen HTML kodu BeautifulSoup ile çözümlenir.
3. <h3> etiketli başlıklar alınır.
4. Başlıklar pandas DataFrame'e aktarılır.
5. Sonuçlar haber_basliklari.csv ve WordCloud görseli olarak kaydedilir.

## ✨ Hazırlayan
**Aleyna Yıldız**
Techİstanbul Python Bootcamp – Bitirme Projesi
Kasım 2025
