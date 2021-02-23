import requests
from lxml import etree
import pickle
url = 'https://www.taicishe.com'
page = requests.get('https://www.taicishe.com/tv-rick-and-morty-2013')
page.encoding = page.apparent_encoding
page = etree.HTML(page.text)
eps = page.xpath('//*[@id="main"]/div/div[2]/div[2]/div/div/div//li')
results = {}

def get_article(url):
    m = requests.get(url)
    m.encoding = m.apparent_encoding
    m = etree.HTML(m.text)
    return m.xpath('//textarea/text()')[0]

season = 1
for i in eps:
    name = i.xpath('a/text()')[0]
    eps_url = url + i.xpath('a/@href')[0]
    content = get_article(eps_url)
    if name[:2] == '1.':
        s = results[season] = {}
        season +=1
    s[name] = content
    print(name, 'succeed!!!')


with open('data', 'wb') as f:
    pickle.dump(results, f)