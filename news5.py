import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd, json

url = "https://www.securitylab.ru/news/"
r = requests.get(url, timeout=(20))

soup = BeautifulSoup(r.text, "html.parser")
article_cards = soup.find_all("a", class_="article-card")
articles = []

for article in article_cards:
    title = article.find("h2", class_="article-card-title").text.strip()

    article_date_time = article.find("time").get("datetime")
    date_from_iso = datetime.fromisoformat(article_date_time)
    date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")

    link = f'https://www.securitylab.ru/{article.get("href")}'
    
    print(title, date_time, link)

    articles.append({'Заголовок': title, 'Дата и время': date_time, 'Ссылка': link})
    
df = pd.DataFrame(articles)
df.to_csv('securitylab_news1.csv', index=False)

with open('securitylab_news1.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)

    

