import requests
from bs4 import BeautifulSoup

def extract_url(url):

    if url.find("www.amazon.com") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.com" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.com" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}

def get_converted_price(price):
    stripped_price = price.strip("$ ,")
    replaced_price = stripped_price.replace(",", "")
    converted_price = float(replaced_price)

    return converted_price

print(get_converted_price("$50.00"))