from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content

Soup = BeautifulSoup(site, 'html.parser')

print(Soup.p.string)
print(Soup.title.string)