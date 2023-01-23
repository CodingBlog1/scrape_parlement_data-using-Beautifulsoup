import requests
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame()
url = 'https://www.parlement-wallonie.be/pwpages?p=pub-new'

re = requests.get(url)

soup  = BeautifulSoup(re.content,'html.parser')

tabel = soup.find('table',class_='table table-condensed table-striped')
# print(a)
tbody = tabel.find('tbody')
# print(tbody)
for i in tbody.find_all('tr'):
    Text_url =  i.find('h5').get_text()
    pdf_url = i.find('a').get('href')
    title = i.find('p').get_text()
    date = i.find('span',class_='text-pw-date').get_text()
    para = i.findAll('p')
    paragraph = para[1].get_text()
    df1 = pd.DataFrame.from_dict([{'Date':date,'Title':title,'Text_url': Text_url, 'Pdf_url': pdf_url, 'Paragraph': paragraph}])
    df = pd.concat([df, df1])

df.to_excel('parlemnt.xlsx')
    