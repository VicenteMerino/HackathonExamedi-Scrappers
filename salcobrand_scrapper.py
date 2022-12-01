from bs4 import BeautifulSoup
from requests import get as GET
from random import randint
from time import sleep
from contextlib import suppress
import json

class SalcobrandScrapper:
    LINKS = [
    ]
    SOURCE = "salcobrand"

    def __init__(self, id) -> None:
        self._id = id

    def get_html(self, url):
        return GET(url).text

    def get_soup(self, html):
        return BeautifulSoup(html, "html.parser")

    def get_price(self, soup):
        try:
            return int(
                soup.find("p", {"class": "sbpay-price"})
                .text.split()[1].replace("$", "")
                .replace(".", "")
                .replace("\n", "")
                .strip()
            )
        except:
            return int(
                soup.find("p", {"class": "normal withoutSbpay"})
                .text.split()[1].replace("$", "")
                .replace(".", "")
                .replace("\n", "")
                .strip()
            )

    def get_active_principle(self, soup):
        return ["ESCITALOPRAM OXALATO"]

    def get_img(self, soup):
        return soup.find("img", {"class": "img-responsive target-image"})["src"]

    def get_name(self, soup):
        return soup.find("h1", {"class": "product-name product_name_pdp"}).text.replace("\n", "").strip()

    def parse_data(self):
        data_to_save = []
        for link in self.LINKS:
            with suppress(Exception):
                html = self.get_html(link)
                soup = self.get_soup(html)
                data = {
                    "id": self._id,
                    "name": self.get_name(soup),
                    "price": self.get_price(soup),
                    "active_principle": self.get_active_principle(soup),
                    "img": self.get_img(soup),
                    "source": self.SOURCE,
                    "link": link
                }
                data_to_save.append(data)
                sleep(0.01)
        return data_to_save
