import requests
from bs4 import BeautifulSoup as BS 
from urllib.parse import quote
import sqlite3

url = 'https://101hotels.com/main/cities/moskva'
r = requests.get(url)
soup = BS(r.content, 'html.parser')

def main():
    total_pages = get_total_pages()
    items_per_page = 10  
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS hotels
                 (address text, price text, name text, link text)''')

    for page in range(1, total_pages + 1):
        data = find(page, items_per_page)
        pras1 = fin_pras(page, items_per_page)
        name1 = name(page, items_per_page)
        links = motiva4ia(page, items_per_page)

        for d, p, n, l in zip(data, pras1, name1, links):
            c.execute("INSERT INTO hotels VALUES (?, ?, ?, ?)", (d, p, n, l))

    conn.commit()
    conn.close()

def find(page, items_per_page):
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    data = soup.find_all('span', class_='item-address')
    return [item.text for item in data[start_index:end_index]]

def fin_pras(page, items_per_page):
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    pras1 = soup.find_all('span', class_='price-value price-highlight')
    return [item.text for item in pras1[start_index:end_index]]

def name(page, items_per_page):
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    name1 = soup.find_all('span', itemprop='name')
    return [item.text for item in name1[start_index:end_index]]

def motiva4ia(page, items_per_page):
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    links = [link['href'] for link in soup.find_all('a') if link.get('href') and link['href'].endswith('html')]
    return links[start_index:end_index]

def get_total_pages():
    return 100

if __name__ == '__main__':
    main()