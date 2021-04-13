import requests
from bs4 import BeautifulSoup

url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'

res = requests.get(url)

res = res.text

soup = BeautifulSoup(res, 'html.parser')



td = soup.find_all("table")

print (td)

# Not sure how to get the td value from the table. I would like to get a standard answer to study.

