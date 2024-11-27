import time
from bs4 import BeautifulSoup
import requests, csv
import pandas as pd


# ----- English Books -----

response = requests.get('https://diwanegypt.com/product-category/books/english-adults/')
src = response.text
soup = BeautifulSoup(src, 'lxml')
# print(response.status_code)
pages = soup.find_all('a', class_='page-numbers')
lastPage = int(pages[-2].text)

allNames = []
allAuthors = []
allPrices = []

for page in range(2,lastPage + 1):
    # bookPrice = soup.find_all('bdi')[0].text
    for name in soup.find_all('h2', attrs={'class': 'woocommerce-loop-product__title'}):
        allNames.append(name.get_text())
    for author in soup.find_all('span', attrs={'class': 'author'}):
        allAuthors.append(author.get_text())
    for price in soup.find_all('span', attrs={'class': 'price'}):
        allPrices.append(price.get_text())

    response = requests.get('https://diwanegypt.com/product-category/books/english-books/' + 'page/' + str(page) + '/')
    # time.sleep(2)
    soup = BeautifulSoup(response.content, 'html.parser')

with open('diwanEnglishBooks.csv', 'w', encoding='utf-8' ,newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['Name', 'Author', 'Price'])
    writer.writeheader()
    for i in range(len(allNames)):
        writer.writerow({'Name': allNames[i], 'Author':allAuthors[i], 'Price':allPrices[i]})

df1 = pd.read_csv('diwanEnglishBooks.csv')
print(df1)

# ----- Arabic Books -----

response = requests.get('https://diwanegypt.com/product-category/books/arabic-books/')
src = response.text
soup = BeautifulSoup(src, 'html.parser')
# print(response.status_code)
pages = soup.find_all('a', class_='page-numbers')
lastPage = int(pages[-2].text)

allNames = []
allAuthors = []
allPrices = []

for page in range(2,lastPage + 1):

    for name in soup.find_all('h2', attrs={'class': 'woocommerce-loop-product__title'}):
        allNames.append(name.get_text())
    for author in soup.find_all('span', attrs={'class': 'author'}):
        allAuthors.append(author.get_text())
    for price in soup.find_all('span', attrs={'class': 'price'}):
        allPrices.append(price.get_text())

    response = requests.get('https://diwanegypt.com/product-category/books/arabic-books/' + 'page/' + str(page) + '/')
    # time.sleep(2)
    soup = BeautifulSoup(response.content, 'lxml')

with open('diwanArabicBooks.csv', 'w', encoding='utf-8' ,newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['Name', 'Author', 'Price'])
    writer.writeheader()
    for i in range(len(allNames)):
        writer.writerow({'Name': allNames[i], 'Author':allAuthors[i], 'Price':allPrices[i]})

df2 = pd.read_csv('diwanArabicBooks.csv')
print(df2)