import sqlite3
import time
import requests


def check_database(offer):
    offer_id = offer["offer_id"]
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL, :url, :offer_id, :date, :price,
                    :address, :area, :rooms, :floor, :total_floor)
            """, offer)
            connection.commit()
            print(f'Объявление {offer_id} добавлено в базу данных')


def main():
    pass


if __name__ == '__main__':
    main()