import requests
from selectolax.parser import HTMLParser as HP #да да хюлет пакарт ака эйч пи ака ноутбуки XD
from fake_useragent import UserAgent
import json
# import csv
import time


#юсер агент
ua = UserAgent()
headers = {'User-Agent': ua.opera}

#запись в файл
# def write_to_csv(filename, data):
#     with open(filename, 'a', encoding = 'utf-8', newline = '') as file:
#         csv.DictWriter(file, filednames = list(data)).writerow(data)



#достаем все нужное
def get_offers(r):
    r.encoding = 'utf-8'
    html = r.text

    tree = HP(html)
    script = tree.css_first('script[id="initial_state_script"]').text()
    script = script[23:-1]

    data = json.loads(script)

    try:
        page_numb = data['routing']['locationBeforeTransitions']['query']['page'][1]
    except:
        page_numb = 0

    #фигня для настройки (не трогать)
    # with open('scrip.json', 'w', encoding='utf-8') as file:
    #     json.dump(data, file, ensure_ascii=False,)

    offers = data['map']['offers']['points']
    
    #вот это вот фор достает нужное настраивается все через него
    for offer in offers:
        url_off = offer['url']
        area = offer['area']['value']
        price = offer['price']['value']
        adres = offer['location']['address']
        
        #тоже нужная вещь для настройки(в идиале не трогать)
        print(area, price, url_off, adres, sep=', ')

        # data_offer = {
        #     'adress': adres,
        #     'area': area,
        #     'price': price,

        # }

        # write_to_csv('yandexpars.csv', data_offer)

        time.sleep(30)
        
    return page_numb


def main():
     page = 1

     while True:
        params = (
               ('page', page),
          )
        
        url = 'https://realty.ya.ru/moskva/snyat/kvartira/bez-posrednikov/?page=1'
        
        r = requests.get(url, params=params, headers=headers)
        page_numb = get_offers(r)

        if page > int(page_numb):
            break
        page += 1


if __name__ == '__main__':
    main()