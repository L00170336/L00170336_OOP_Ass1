# Anne O'Brien
# Student ID: L00170336
# OOP Assignment1_Question 2


# Import beautiful soup packages
import requests
import bs4

# URL for my Ubuntu server that I am going to parse
r = requests.get('http://192.168.220.129/')

# import beautifulsoup which will go get the headings
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

headers = soup.find_all("div", {"class": "section_header"})
print(headers)




