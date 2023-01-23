import pandas as pd
import requests
from bs4 import BeautifulSoup

# base_url = 'https://www.vlaamsparlement.be/nl/parlementair-werk/documenten/alle-documenten'
# url = 'https://www.vlaamsparlement.be/nl/parlementair-werk/documenten/alle-documenten?page=2'




li=[]
def data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    h = soup.findAll('div',class_='card__header-inner-wrapper')
    for i in h:
        li.append(i.find('div').get_text())
        print(i.find('div').get_text())
   # print(h.find('div').get_text())
for  i in range(0,20):
    url = f'https://www.vlaamsparlement.be/nl/parlementair-werk/documenten/alle-documenten?page={str(i)}'
    if url:
        data(url)
    else:
        break
print(li)