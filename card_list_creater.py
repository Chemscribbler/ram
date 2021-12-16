import requests
import csv


def main():
    root_address = "https://netrunnerdb.com/api/2.0/"

    # Custom disallowed packs
    invalid_pack_codes = [
        "tdc",
        "dag",
        "bm",
        "urbp",
        "mo",
        "sc19",
        "su21",
        "napd",
        "draft",
    ]

    response = requests.get(root_address + "public/cards")

    cards = response.json()["data"]

    with open("cards.csv", "w") as f:
        file = csv.writer(f)
        for card in cards:
            if card["pack_code"] not in invalid_pack_codes:
                try:
                    file.writerow(
                        [
                            card["stripped_title"],
                            card["faction_code"],
                            card["type_code"],
                            card["pack_code"],
                            card["text"],
                            card["keywords"],
                        ]
                    )
                except:
                    file.writerow(
                        [
                            card["stripped_title"],
                            card["faction_code"],
                            card["type_code"],
                            card["pack_code"],
                        ]
                    )


if __name__ == "__main__":
    main()
