import requests
import fake_useragent
from bs4 import BeautifulSoup

url = 'https://www.skiddle.com/festivals/'

ua = fake_useragent.UserAgent()

headers = {
    'User-Agent': ua.random
}

req = requests.get(url, headers=headers)

# создаем объеккт soup и находим все теги <a> которые лежат внутри таблицы со списком фестивалей
soup = BeautifulSoup(req.text, 'lxml')
all_fest_link = soup.find(class_='search-body').find_all('a')

# получаем ссылки на все фестивали
fest_urls_links = []
for link in all_fest_link:
    url = link.get('href')
    if link.get('href') is not None:
        fest_url = 'https://www.skiddle.com' + url
        fest_urls_links.append(fest_url)