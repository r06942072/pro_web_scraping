from selenium import webdriver
import requests
import bs4

print("capture from Wikipedia")

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(soup))

titles = soup.select('.mw-headline') #class = mw-headline
print(type(titles))

for i in titles:
	print(type(i))
	print(i.text)
