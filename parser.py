import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://schoolhm.ru/10-%D0%BA%D0%BB%D0%B0%D1%81%D1%81-%D1%8E%D1%84%D0%BC%D0%BB/', verify=False)
html = BS(r.content, 'html.parser')

text_site = []
href_site = []

for el in html.select('.entry-content'):
    text_site.append(el.text.replace('\xa0', ' ').split('\n'))

for el in html.find_all('a', href=True):
    href_site.append(*el.text.replace('\xa0', ' ').split('\n'))

print(text_site)
print(href_site)

print(len(text_site[0]))
print(len(href_site))

