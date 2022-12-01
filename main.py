import json
from random import randint
from ahumada_scrapper import AhumadaScrapper
from farmex_scrapper import FarmexScrapper
from salcobrand_scrapper import SalcobrandScrapper

if __name__ == "__main__":
    _id = randint(1, 10000000)
    ahumada_scrapper = AhumadaScrapper(_id)
    farmex_scrapper = FarmexScrapper(_id)
    salcobrand_scrapper = SalcobrandScrapper(_id)

    data = []
    data.extend(ahumada_scrapper.parse_data())
    data.extend(farmex_scrapper.parse_data())
    data.extend(salcobrand_scrapper.parse_data())
    print(data)

    with open(f"{_id}_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)