import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical'
    res = requests.get(url)
    res = res.text
    soup = BeautifulSoup(res, 'html.parser')

    print(soup)

if __name__ == '__main__':
        main()

#unable to get the html from nasdaq