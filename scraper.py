import requests
from bs4 import BeautifulSoup

url = input("Enter URL:")
data = requests.get(url).text

soup = BeautifulSoup(data, "lxml")

for link in soup.find_all("p"):
    print((link.get_text()).strip())
