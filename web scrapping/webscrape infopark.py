import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page=requests.get(url)
soup=BeautifulSoup(page.text,'lxml')
tab=soup.find('table',class_='wikitable sortable')
# x=soup.find('table',{'class':'wikitable sortable'})
heading=tab.find_all('th')
headings=[title.text.strip() for title in heading]

df=pd.DataFrame(columns=headings)
rows=tab.find_all('tr')
for rowdata in rows[1:]:
    data=[datas.text.strip() for datas in rowdata]
    data=[dat for dat in data if dat!='']
    length=len(df)
    df.loc[length]=data
print(df)
df.to_csv("D:\VSCode\python prgrms\Data Analytics\data.csv", index=False)