from bs4 import BeautifulSoup as Bsoup
from urllib.request import urlopen

my_url = "https://morvanzhou.github.io/static/scraping/list.html"
page_html = urlopen(my_url).read().decode('utf-8')
#print(page_html)

## html parsing
page_soup = Bsoup(page_html, "html.parser")
#print(page_soup)

## use class to narrow search
## function find_all, setting two searching constraints
parse_month = page_soup.find_all('li', {"class": "month"})
parse_month = page_soup.find_all('ul', {"class": "jan"})
print(parse_month)
for m in parse_month:
    print(m.get_text())
