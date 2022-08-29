import classes as dnd
import sys


def gather_party(theme):
    if theme == "arcane":
        return dnd.random_party_with_matching_primary("int")
    elif theme == "shady":
        return dnd.random_party_with_matching_primary("dex")
    elif theme == "brutes":
        return dnd.random_party_with_matching_primary("str")
    elif theme == "brawn":
        return dnd.random_party_with_matching_primary("con")
    elif theme == "wise":
        return dnd.random_party_with_matching_primary("wis")
    elif theme == "face":
        return dnd.random_party_with_matching_primary("cha")
    else:
        return dnd.random_party_with_matching_primary("str")


def collect_args():
    config = {}
    config["dc"] = sys.argv[1]
    config["party"] = sys.argv[2]
    return config


def attempts_to_find_the_path(dc, party):
    party = gather_party(party)

    print(party)
    print(dc)
    return 0


def main():
    config = collect_args()
    attempts_to_find_the_path(config["dc"], config["party"])


if __name__ == "__main__":
    main()
