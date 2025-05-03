from bs4 import BeautifulSoup
import requests


def currencyExchange(from_curr,to_curr):
    url=f"https://www.x-rates.com/calculator/?from={from_curr}&to={to_curr}&amount=1"
    content=requests.get(url).text
    soup=BeautifulSoup(content,'html.parser')
    rate=soup.find("span",class_="ccOutputRslt").text
    return float(rate[:-4])

rate=(currencyExchange("EUR","INR"))
print(rate)