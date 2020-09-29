from bs4 import BeautifulSoup
import requests
import time
import csv

URL = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"


def get_price():
    source = requests.get(URL).text
    soup = BeautifulSoup(source, "lxml")
    current_price = soup.find("span", "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" ).get_text()

    with open ('price.csv', 'a') as prices:
        csv_writer = csv.writer(prices, delimiter=',')
        csv_writer.writerow(current_price)
    print(current_price)


    

while True:
    get_price()
    time.sleep(2)



