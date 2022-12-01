from bs4 import BeautifulSoup
from requests import get as GET
from random import randint
from time import sleep
from contextlib import suppress
import json



class AhumadaScrapper:
    LINKS = [
        "https://www.farmaciasahumada.cl/lexapro-20-mg-x-28-comprimidos-recubiertos.html",
        "https://www.farmaciasahumada.cl/escitavitae-20-mg-x-28-comprimidos-recubiertos.html"
    ]
    SOURCE = "ahumada"
    def __init__(self, id) -> None:
        self._id = id

    def get_html(self, url):
        return GET(url).text


    def get_soup(self, html):
        return BeautifulSoup(html, "html.parser")


    def get_price(self, soup):
        return int(
            soup.find("span", {"class": "special-price"})
            .text.replace("$", "")
            .replace(".", "")
            .replace("\n", "")
            .strip()
        )


    def get_active_principle(self, soup):
        p = soup.find("td", {"data-th": "Principio Activo"}).text
        active_principle = [_.strip() for _ in p.split("-") if _]
        return active_principle


    def get_img(self, soup):
        return soup.find("img", {"class": "gallery-placeholder__image"})["src"]


    def get_name(self, soup):
        return soup.find("span", {"class": "base"}).text

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
                    "link": link,
                }
                data_to_save.append(data)
                sleep(0.01)
        return data_to_save
