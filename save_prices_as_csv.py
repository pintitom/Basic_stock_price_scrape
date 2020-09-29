from bs4 import BeautifulSoup
import requests
import time
import csv
import os.path

aapl_url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
csco_url = "https://finance.yahoo.com/quote/CSCO?p=CSCO&.tsrc=fin-srch"
ko_url = "https://finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch"


if os.path.exists("prices.csv"):
    pass
else:
    with open("prices.csv","w", newline='') as prices:
        csv_writer = csv.writer(prices)
        csv_writer.writerow(["AAPL","CSCO","KO"])    

def get_price(URL):
    source = requests.get(URL).text
    soup = BeautifulSoup(source, "lxml")
    current_price = soup.find("span", "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" ).get_text()
    return current_price

def apend_to_csv(aapl_price,csco_price,ko_price):
    with open("prices.csv","a", newline='') as prices:
        csv_writer = csv.writer(prices)
        data =[aapl_price, csco_price, ko_price]
        csv_writer.writerow(data)

while True:
    aapl_price = get_price(aapl_url)
    csco_price = get_price(csco_url)
    ko_price = get_price(ko_url)
    apend_to_csv(aapl_price,csco_price,ko_price)
    print(list([aapl_price,csco_price,ko_price]))
    time.sleep(900)