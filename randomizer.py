import requests
import random


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

    # Custom Defined Bix Boxes
    big_box_sets = ["core", "cac", "hap", "oac", "dad", "td", "core2", "rar", "sg"]

    # Request the list of packs, then randomly draw 2 big box sets

    seed_input = input("Random Seed: ")
    random.seed(seed_input)

    response = requests.get(root_address + "public/packs")

    packs = response.json()["data"]

    invalid_pack_codes.extend(big_box_sets)

    # Exclude the big boxes and banned packs
    filtered_packs = [
        {"code": pack["code"], "name": pack["name"], "release": pack["date_release"]}
        for pack in packs
        if pack["code"] not in invalid_pack_codes
    ]

    big_box_sets = [
        {"code": pack["code"], "name": pack["name"], "release": pack["date_release"]}
        for pack in packs
        if pack["code"] in big_box_sets
    ]

    cores = random.sample(big_box_sets, 2)
    cores.sort(key=lambda x: x["release"])

    boosters = random.sample(filtered_packs, 13)
    boosters.sort(key=lambda x: x["release"])

    ordered_list = cores.copy()
    ordered_list.extend(boosters)

    nrdb_filter = f"e:{'|'.join([card_set['code'] for card_set in ordered_list])}"
    human_list = f"{chr(10).join([card_set['name'] for card_set in ordered_list])}"
    print(nrdb_filter)
    print(human_list)


if __name__ == "__main__":
    main()