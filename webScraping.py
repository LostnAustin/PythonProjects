iport urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlliv.request.urlopen(url.read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
  print(tag.get('href', None))
