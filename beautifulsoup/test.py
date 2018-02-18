from bs4 import BeautifulSoup
import urllib

start_url = 'http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20'
html = urllib.urlopen(start_url).read()

soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all("#innerHTML")
print titles
for title in titles:
    print title.text