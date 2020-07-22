import bs4
from datetime import datetime
import requests
import constant

now = datetime.now()
html = requests.get(constant.URL_TO_GRAB).content
soup = bs4.BeautifulSoup(html, 'html.parser')

content = soup.find("div", class_="application-main")

filename = "dataBuffer/" + now.__str__() + ".txt"
f = open(filename, "w+")
f.write(content.__str__())
f.close()

print(constant.URL_TO_GRAB + ' > ' + filename)
