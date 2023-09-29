import requests
import json


def main():

    cookies = {
        '_CIAN_GK': '9d66b944-53e9-442a-af09-9ad7b928cdbf',
        'session_region_id': '1',
        '__cf_bm': 'J.PE7lY6fc535pJgzQ32VhtBqBoX8bZ5NCvST1EF6hM-1696012885-0-Aa0heQ1aXQQby1JX5cYM4V7b9yTjywFFiVENfKwJy0yn4prYBSbxaM2WE8VWyzJE/GaZjNzcdePwCXJCyByrgjg=',
        '_gcl_au': '1.1.2138522105.1696012887',
        'tmr_lvid': '83611a91c21d2c09c7cdd5d23b73519b',
        'tmr_lvidTS': '1696012887313',
        'login_mro_popup': '1',
        'sopr_utm': '%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
        'sopr_session': 'e01339fa3d194929',
        'uxfb_usertype': 'searcher',
        '_ym_uid': '1696012888511879612',
        '_ym_d': '1696012888',
        'uxs_uid': 'ccd7eca0-5ef7-11ee-b8f8-fbdb390f816b',
        '_ym_isad': '2',
        '_gid': 'GA1.2.1271640860.1696012888',
        '_ym_visorc': 'b',
        'adrdel': '1',
        'adrcid': 'AhSCQ9flahJrdG15TbOjoaQ',
        'afUserId': 'd99519c9-224f-4c72-ad40-3054b0927538-p',
        'AF_SYNC': '1696012888983',
        'session_main_town_region_id': '1',
        'viewpageTimer': '108.01599999999999',
        '_ga': 'GA1.2.637072536.1696012888',
        '_dc_gtm_UA-30374201-1': '1',
        '_ga_3369S417EL': 'GS1.1.1696012888.1.1.1696013122.60.0.0',
    }

    headers = {
        'authority': 'api.cian.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': '_CIAN_GK=9d66b944-53e9-442a-af09-9ad7b928cdbf; session_region_id=1; __cf_bm=J.PE7lY6fc535pJgzQ32VhtBqBoX8bZ5NCvST1EF6hM-1696012885-0-Aa0heQ1aXQQby1JX5cYM4V7b9yTjywFFiVENfKwJy0yn4prYBSbxaM2WE8VWyzJE/GaZjNzcdePwCXJCyByrgjg=; _gcl_au=1.1.2138522105.1696012887; tmr_lvid=83611a91c21d2c09c7cdd5d23b73519b; tmr_lvidTS=1696012887313; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D; sopr_session=e01339fa3d194929; uxfb_usertype=searcher; _ym_uid=1696012888511879612; _ym_d=1696012888; uxs_uid=ccd7eca0-5ef7-11ee-b8f8-fbdb390f816b; _ym_isad=2; _gid=GA1.2.1271640860.1696012888; _ym_visorc=b; adrdel=1; adrcid=AhSCQ9flahJrdG15TbOjoaQ; afUserId=d99519c9-224f-4c72-ad40-3054b0927538-p; AF_SYNC=1696012888983; session_main_town_region_id=1; viewpageTimer=108.01599999999999; _ga=GA1.2.637072536.1696012888; _dc_gtm_UA-30374201-1=1; _ga_3369S417EL=GS1.1.1696012888.1.1.1696013122.60.0.0',
        'origin': 'https://www.cian.ru',
        'referer': 'https://www.cian.ru/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'jsonQuery': {
            '_type': 'flatrent',
            'sort': {
                'type': 'term',
                'value': 'creation_date_desc',
            },
            'engine_version': {
                'type': 'term',
                'value': 2,
            },
            'region': {
                'type': 'terms',
                'value': [
                    1,
                ],
            },
            'for_day': {
                'type': 'term',
                'value': '!1',
            },
            'room': {
                'type': 'terms',
                'value': [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    9,
                ],
            },
        },
    }

    response = requests.post(
        'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"jsonQuery":{"_type":"flatrent","sort":{"type":"term","value":"creation_date_desc"},"engine_version":{"type":"term","value":2},"region":{"type":"terms","value":[1]},"for_day":{"type":"term","value":"!1"},"room":{"type":"terms","value":[1,2,3,4,5,6,7,9]}}}'
    #response = requests.post(
    #    'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,

    data = response.json()

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False,)




if __name__ == '__main__':
    main()