import requests
import pandas as pd
from bs4 import BeautifulSoup

page_num = 1
names2 = []
raw_data = [[],[],[]]

page = requests.get('https://nextspaceflight.com/launches/past/?page='+ str(page_num))
soup = BeautifulSoup(page.content, 'html.parser')
for a in soup.find_all('a', href=True):
    print("Found the URL:", a['href'])




'''while True:
    page = requests.get('https://nextspaceflight.com/launches/past/?page='+ str(page_num))
    soup = BeautifulSoup(page.content, 'html.parser')
    names = soup.find_all('h5')
    times = soup.find_all('div',{'class': "mdl-card__supporting-text"})
    orgs = soup.find_all('div',{'class': "mdl-card__title-text"})
    if(names == names2):
        break
    names2 = names
    raw_data[0] += names
    raw_data[1] += times
    raw_data[2] += orgs
    page_num += 1

final_data = []
for i in range(0, len(raw_data[0])):
    rocket = raw_data[0][i].get_text().split('\n')[1].split('|')[0].strip()
    mission = raw_data[0][i].get_text().split('\n')[1].split('|')[1].strip()
    time = raw_data[1][i].get_text().strip().split("\n")[0].strip()
    loc = raw_data[1][i].get_text().strip().split("\n")[-1].strip()
    org = raw_data[2][i].get_text().strip()
    final_data.append([rocket, mission, org, time, loc])

df = pd.DataFrame(final_data)
df.to_csv('launches.csv', index=False, header=False)'''