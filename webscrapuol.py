from bs4 import BeautifulSoup
import requests

url = 'https://www.uol.com.br'

response = requests.get(url)
print(response.status_code)

sp = BeautifulSoup(response.text, 'html.parser')

contents = sp.find_all(attrs={'class':'section__grid__main__rows'})

sp

for p in contents:
    links = p.find_all('a', href=True)
    for link in links:
        print(f"Titulo da noticia: {link.text.strip()}")
        print(f"Link: {link['href']}\n")