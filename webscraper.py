import requests
import pandas as pd
import lxml
from bs4 import BeautifulSoup


def parse_page(full_url='https://nextspaceflight.com/launches/details/100'):
    '''
    Given a page in the nextspaceflight.com detailed format, extracts a set of
    data including the details listed below in stat_list. Data is formatted as
    text and added to an output list.

    Params:
        full_url: the full url to the page to extract data from, including the
        url and the page

    Returns:
        a list of all the stats extracted from the page
    '''
    stat_list = ['Rocket', 'Mission', 'Org', 'Outcome', 'Location', 'Time',
                 'Price', 'Status', 'Liftoff Thrust', 'Rocket Height',
                 'Stages', 'Strap-ons']
    data = [None] * 12
    page = requests.get(full_url)
    soup = BeautifulSoup(page.text, 'lxml')

    data[0] = soup.find('div',
                        {'class': 'mdl-card__title-text'}).get_text().strip()
    data[1] = soup.find('h4',
                        {'class': 'mdl-card__title-text'}).get_text().strip()
    try:
        data[3] = soup.find('h6',
                            {'class': 'rcorners status'}).get_text().strip()
    except:
        data[3] = None
    data[5] = soup.find(text='Launch Time') \
                  .find_next().find_next(text=True).strip()
    data[4] = soup.find(text='Location').find_next('h4').get_text()
    stats = soup.find('div', {'class': 'mdl-grid a', 'style': 'margin: -20px'})
    children = stats.findChildren()
    for child in children:
        text = child.get_text().strip().split(":")
        if len(text) == 1:
            data[2] = text[0]
        elif text[0] in stat_list:
            data[stat_list.index(text[0])] = text[1].strip()
    return data


def parse_website(url='https://nextspaceflight.com/launches/details/',
                  limit=200):
    '''
    Given a full url and page, iterates numerically through pages at the url
    and uses parse_page to find the data in that page and add it to a full
    list of all stats. Pages are in the format url/1, url/2, etc.

    Params:
        url: the url to find pages containing the data
        limit: the number of consecutive nonexistent pages to accept before
        the function returns. This is useful if there are unavailible pages
        in the middle of the data.

    Returns:
        A 2D list of all data, each page being a row and the columns being
        organized as in parse_page
    '''
    page_num = 0
    fail = 0
    data = []
    while True:
        page = url + str(page_num)
        if page_num % 500 == 0:
            print('Scanned', page_num, 'pages')
        page_num += 1
        try:
            data.append(parse_page(page))
            fail = 0
        except:
            fail += 1
            if fail > limit:
                break
    return data


def make_csv(pathname):
    '''
    Given a name and path for a csv file, creates a dataframe using the
    parse_website function and outputs it to a csv

    Params:
        pathname: the file path and name of the csv file. If it doesn't
        already exist, a new one is created, otherwise the existing file
        is overwritten
    '''
    df = pd.DataFrame(parse_website())
    df.to_csv(pathname, index=False, header=False)
