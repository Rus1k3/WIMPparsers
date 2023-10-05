import requests
from selectolax.parser import HTMLParser as HP #да да хюлет пакарт ака эйч пи ака ноутбуки XD
from fake_useragent import UserAgent
import json
import os
import random
import sys
import sqlite3


# Создание соединения с базой данных (или ее создание, если она не существует)
conn = sqlite3.connect('offers.db')

# Создание курсора для выполнения SQL-запросов
c = conn.cursor()

# Создание таблицы, если она еще не существует
c.execute('''
    CREATE TABLE IF NOT EXISTS offers
    (url TEXT, area REAL, price REAL, address TEXT)
''')


#прокси сервера
proxies = {
  'https': 'http://SywsYG:W236W7@45.91.209.157:10234',
}
#путь к каталогу где сохраняется файл scrip.json
current_dir = os.getcwd()

#юсер агент
ua = UserAgent()
headers = {'User-Agent': ua.opera}

# получение количества страниц

page_rndm = str(random.randint(99, 999))

url = 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?page=' + page_rndm
response = []
response = requests.get(url, proxies=proxies)

# проверка на капчу (Если её нет то записывается кол-во страниц)

if response.url[21] == 's' and response.url[31] == 'a':
    print('БЛЯ КАПЧА')
    sys.exit()
else:
    fi = str(response.url[-2])
    se = str(response.url[-1])
    x = int(fi + se)
    print('КОЛЛИЧЕСТВО СТРАНИЦ - ', x)

def main():
    read_file()

def create_file():

    html = r.text

    tree = HP(html)
    script = tree.css_first('script[id="initial_state_script"]').text()
    script = script[23:-1]

    data = json.loads(script)

    with open('scrip.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False,)

def read_file():

    create_file()

    file_js = json.load(open('scrip.json', 'r', encoding='utf-8'))

    offers = file_js['map']['offers']['points']

    for offer in offers:

        url_off = offer['url']
        area = offer['area']['value']
        price = offer['price']['value']
        address = offer['location']['address']

        # Вставка данных в таблицу
        c.execute('''
            INSERT INTO offers (url, area, price, address)
            VALUES (?, ?, ?, ?)
        ''', (url_off, area, price, address))

    # Сохранение изменений
    conn.commit()



y = 0
z = 1
while x > y:
    
    print('СТРАНИЦА - ', y + 1)

    z = str(z)

    url = 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?page=' + z
    z = int(z)
    if z % 3 == 0:
        proxies = {
        'https': 'http://XQmL0w:zcyPdR@85.195.81.143:10776',
        }
    elif z % 2 == 0:
        proxies = {
        'https': 'http://SywsYG:W236W7@45.91.209.157:10234',
        }
    else:
        proxies = {
        'https': 'http://9j67JM:4tx0B5@217.29.62.211:13336',
        }


    r = requests.get(url, headers=headers, proxies=proxies)

    if __name__ == '__main__':
        main()
    
    z+=1
    y+=1
    
print('все страницы спарсились')
conn.close()