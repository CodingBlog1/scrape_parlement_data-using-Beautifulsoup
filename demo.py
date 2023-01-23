from bs4 import BeautifulSoup
import requests
import pandas as pd

# df = df.append({'name': i, 'age': i, 'height': i}, ignore_index=True) 

df = pd.DataFrame()
url_list = []
href_link = []
href_text = []
para = []
url = 'https://cnpd.public.lu/fr/decisions-sanctions.html'
count = 0

# for main url 
def to_find(url, count): 
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    if count == 0:
        page = soup.find('ol',class_='pagination')
        a = page.findAll('li',class_='pagination-page')
        page = soup.find('ol',class_='pagination')
        a = page.findAll('li',class_='pagination-page')
        for  i in a[1:]:
            # print(i)
            url_list.append(i.find('a').get('href'))
            count += 1
        # print('url_list',url_list)
    scrap_data(soup)


# scrap data
def scrap_data(soup):
    global df
    a = soup.find('ol',class_='search-results')
    # print(a)
    all_div = a.find_all('div',class_='mo-body')
    # print(all_div)
    for  i in all_div:
        href = i.find('a').get('href')
        href_txt = i.find('h2').get_text()
        paragraph = i.find('p').get_text()
        time = i.find('time').get_text()
        # print(time)

        # df = df.append({'URL': href, 'href_txt': href_txt, 'paragraph': paragraph}, ignore_index=True) 
        df1 = pd.DataFrame.from_dict([{'Time':time,'URL': href, 'href_txt': href_txt, 'paragraph': paragraph}])
        df = pd.concat([df, df1])
        href_link.append(href)
        href_text.append(href_txt)
        para.append(paragraph)
    # print("href_text",href_text)
    # print("href_link",href_link)
    # print("--------------------------------para------------------")
    # print(len(para),len(href_text),len(href_link))
    # print(df)
    df.to_csv("final.csv")
    df.to_excel("final.xlsx")
    




to_find(url=url, count=count)

# itrate all the pages 
for i in url_list:
    base_url=url.split('/fr/decisions-sanctions.html')
    base_url=base_url[0]
    main_url = f"{base_url}{i}"
    # print(main_url)
    count += 1
    to_find(url=main_url, count=count)






