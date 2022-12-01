import json
URLS = [
    "501092_data.json",
    "2197465_data.json",
    "2438421_data.json",
    "2600706_data.json",
    "3275417_data.json",
    "5522196_data.json",
    "5578874_data.json",
    "7664470_data.json",
    "7942170_data.json"
]
if __name__ == "__main__":
    data = []
    for url in URLS:
        with open(url, "r", encoding="utf-8") as f:
            data.extend(json.load(f))
    with open("merged_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
