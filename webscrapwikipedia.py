from bs4 import BeautifulSoup
import requests

url = 'https://pt.wikipedia.org'

response = requests.get(url)
response.status_code
print(response.status_code)

sp = BeautifulSoup(response.text, 'html.parser')

contents = sp.find_all(attrs={'class':'main-page-block-contents'})[-2]

sp

for p in contents:
    print(p.text)