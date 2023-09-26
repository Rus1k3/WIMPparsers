import requests
from selectolax.parser import HTMLParser as HP #да да хюлет пакарт ака эйч пи ака ноутбуки XD
from fake_useragent import UserAgent
import json
import os


#путь к каталогу где сохраняется файл scrip.json
current_dir = os.getcwd()

#юсер агент
ua = UserAgent()
headers = {'User-Agent': ua.opera}

url = 'https://realty.ya.ru/moskva/kupit/kvartira/bez-posrednikov/?page='

r = requests.get(url, headers=headers)

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
        adres = offer['location']['address']
        
        print(area, price, url_off, adres, sep=', ')



if __name__ == '__main__':
    main()