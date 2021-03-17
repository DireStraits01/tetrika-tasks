import requests
from bs4 import BeautifulSoup
import re

HOST = 'https://ru.wikipedia.org/'
URL = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F' \
      ':%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B' \
      '8%D1%82%D1%83&from=%D0%90'
HEADERS = {
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,ap'
         'plication/signed-exchange;v=b3;q=0.9',
  'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Sa'
               'fari/537.36'
}

def get_html(url,params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_params(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    pages = soup.find('div', {"id": "mw-pages"})
    if pages is None:
        return None
    pages = pages.find_all('a')[1]
    return pages['href']

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='mw-category-group')
    animals = []
    for item in items:
        animals.append(item.find('ul').get_text()) #get animals names from tag <ul>
    return animals

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        pages = get_params(html)
        animals = []
        print(pages)
        #for href in pages:

        while "from=A" not in pages:
            if animals:
                value = get_content(html.text)
                valueLetter = value[0]
                last_letter = animals[-1][0]
                print(valueLetter)
            print(f"parsing letter: {pages}")
            html = get_html(HOST + pages)

            animals.append(get_content(html.text))
            pages = get_params(html)

        return animals[0].count('\n')-1
    else:
        print('Error!')

def get_number_of_animals(alphabet='абв'.upper()):
    count = []
    for x in alphabet:
        count.append(f"{x} : {parser(x)}")
    return ('\n'.join(count))


print(parser())

