import requests
import fake_useragent
import json
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

# получаю данные по каждому фестивалю
fest_list_result = {}
for url in fest_urls_links:
    req = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        fest_name = soup.find('h1', class_='css-r2lffm').text
        fest_info_block = soup.find(class_='css-1ik2gjq')
        fest_date = fest_info_block.find(class_='css-f3i3nk').text
        fest_location = fest_info_block.find(class_='css-1d3bbye').text

        fest_list_result[fest_name] = {
            'fest_date': fest_date,
            'fest_location': fest_location
        }

    except Exception as ex:
        print(ex)
        print('There was some error...')

with open("fest_list_result.json", "w", encoding="utf-8") as file:
    json.dump(fest_list_result, file, indent=4, ensure_ascii=False)
