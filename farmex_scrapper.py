from bs4 import BeautifulSoup
from requests import get as GET
from random import randint
from time import sleep
from contextlib import suppress
import json

LINKS = [
    "https://farmex.cl/products/escitavitae-20-mg-x-28-comprimidos?_pos=5&_sid=0cad1e5c4&_ss=r",
    "https://farmex.cl/products/lexapro-tabletas-escitalopram-20?_pos=19&_sid=0cad1e5c4&_ss=r"
]

class FarmexScrapper:
    def __init__(self, id) -> None:
        self._id = id

    def get_html(self, url):
        return GET(url).text


    def get_soup(self, html):
        return BeautifulSoup(html, "html.parser")


    def get_price(self, soup):
        return int(
            soup.find("div", {"class": "detail-price"})
            .text.replace("$", "")
            .replace(".", "")
            .replace("\n", "")
            .strip()
        )


    def get_active_principle(self, soup):
        return ["ESCITALOPRAM OXALATO"]


    def get_img(self, soup):
        return soup.find("img", {"id": "product-featured-image"})["src"]

    def get_name(self, soup):
        return soup.find("h1", {"class": "page-heading"}).text

    def parse_data(self):
        data_to_save = []
        for link in LINKS:
            with suppress(Exception):
                html = self.get_html(link)
                soup = self.get_soup(html)
                data = {
                    "id": self._id,
                    "name": self.get_name(soup),
                    "price": self.get_price(soup),
                    "active_principle": self.get_active_principle(soup),
                    "img": self.get_img(soup),
                    "source": "farmex",
                    "link": link
                }
                data_to_save.append(data)
                sleep(0.01)
        return data_to_save

if __name__ == "__main__":
    scrapper = FarmexScrapper(1)
    data = scrapper.parse_data()
