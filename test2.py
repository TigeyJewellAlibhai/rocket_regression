import requests
import pandas as pd
import re
import lxml
from bs4 import BeautifulSoup

def parse_page(full_url='https://nextspaceflight.com/launches/details/100'):


    stat_list=['Rocket', 'Mission', 'Org', 'Outcome', 'Location', 'Time', 'Price',
           'Status', 'Liftoff Thrust', 'Rocket Height', 'Stages', 'Strap-ons']
    data=[None] * 12
    page = requests.get(full_url)
    soup = BeautifulSoup(page.text, 'lxml')

    data[0] = soup.find('div', {'class': 'mdl-card__title-text'}).get_text().strip()
    data[1] = soup.find('h4', {'class': 'mdl-card__title-text'}).get_text().strip()
    try:
        data[3] = soup.find('h6', {'class': 'rcorners status'}).get_text().strip()
    except:
        data[3] = None
    data[5] = soup.find(text='Launch Time').find_next().find_next(text=True).strip()
    data[4] = soup.find(text='Location').find_next('h4').get_text()
    stats = soup.find('div',{'class': 'mdl-grid a', 'style': 'margin: -20px'})
    children = stats.findChildren()
    for child in children:
        text = child.get_text().strip().split(":")
        if len(text) == 1:
            data[2] = text[0]
        elif text[0] in stat_list:
            data[stat_list.index(text[0])] = text[1].strip()
    return data

def parse_website(url='https://nextspaceflight.com/launches/details/'):
    
    page_num = 0
    fail = 0
    data = []
    while True:
        print(page_num)
        page = url + str(page_num)
        page_num += 1
        try:
            data.append(parse_page(page))
        except:
            fail += 1
            if fail > 500:
                break
        '''if(requests.get(page).status_code != requests.codes.ok):
            fail += 1
            if fail > 100:
                break
        else:
            fail = 0
            data.append(parse_page(page))'''
    return data


##df = pd.DataFrame(parse_website())
##df.to_csv('launches.csv', index=False, header=False)