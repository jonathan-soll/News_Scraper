# scraping.py

from bs4 import BeautifulSoup
import requests

def scrape():

    url = 'https://seekingalpha.com/market-news/all'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    all_tickers = soup.find_all('li', attrs = {'class' : 'mc'})

    l = []
    for ticker in all_tickers:
        mydict = {}
        symbol_content = ticker.find('a', attrs={'sasource': 'ticker_mc_quote'})

        if symbol_content != None:
            symbol = symbol_content.text
            title = ticker.find_all('div', attrs= {'class' : 'title'})[0].text
            date = ticker.find('span', attrs= {'class' : 'item-date'}).text
    #         print(date + ': ' + symbol + ' - ' + title)
    #         print('')

            mydict['date'] = date
            mydict['symbol'] = symbol
            mydict['title'] = title

        l.append(mydict)

    return l

if __name__ == "__main__":
    print(scrape())
