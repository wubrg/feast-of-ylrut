import random


def random_sub_class(primary_class):
    classes = {
        "fighter": [
            "battle master",
            "champion",
            "arcane_archer",
            "cavalier",
            "eldritch knight",
            "psi warrior",
            "purple dragon knight",
            "rune knight",
            "samurai",
        ],
        "barbarian": [
            "wild magic",
            "totem warrior",
            "zealot",
            "ancestral guardian",
            "battlerager",
            "beast",
            "storm herald",
            "berserker",
        ],
        "paladin": [
            "vengeance",
            "watchers",
            "conquest",
            "devotion",
            "redemption",
            "ancients",
            "glory",
            "crown",
            "oathbreaker",
        ],
        "ranger": [
            "beast master",
            "fey wanderer",
            "hunter",
            "gloom stalker",
            "monster slayer",
            "swarmkeeper",
            "horizon walker",
        ],
        "monk": [
            "mercy",
            "shadow",
            "astral self",
            "kensei",
            "four elements",
            "drunken master",
            "long death",
            "open hand",
            "sun soul",
        ],
        "bard": [
            "creation",
            "glamour",
            "lore",
            "swords",
            "eloquence",
            "spirits",
            "valor",
            "whispers",
        ],
        "rogue": [
            "arcane trickers",
            "assassin",
            "inquisitive",
            "mastermind",
            "thief",
            "phantom",
            "soulknife",
            "swashbuckler",
        ],
        "artificer": ["alchemist", "artillerist", "battle smith", "armorer"],
        "druid": ["dreams", "stars", "wildfire", "land", "moon", "sheperd", "spores"],
        "wizard": [
            "battlesinger",
            "scribes",
            "war magic",
            "abjuration",
            "conjuration",
            "enchantment",
            "divination",
            "evocation",
            "transmutation",
            "necromancy",
            "illusion",
        ],
        "sorcerer": [
            "aberrant mind",
            "divine soul",
            "clockwork soul",
            "draconic bloodline",
            "shadow magic",
            "storm sorcery",
            "wild magic",
        ],
        "cleric": [
            "arcana",
            "death",
            "forge",
            "life",
            "peace",
            "order",
            "grave",
            "knowledge",
            "light",
            "war",
            "nature",
            "twilight",
            "tempest",
            "trickery",
        ],
        "warlock": [
            "archfey",
            "genie",
            "fathomless",
            "fiend",
            "great old one",
            "hexblade",
            "undead",
            "undying",
        ],
    }
    return random.choice(classes[primary_class])


def random_primary_class(primary):
    primaries = {
        "str": ["fighter", "barbarian", "monk", "paladin", "ranger"],
        "dex": ["monk", "bard", "rogue"],
        "con": ["fighter", "barbarian", "sorcerer", "artificer"],
        "int": ["artificer", "rogue", "druid", "wizard"],
        "wis": ["ranger", "druid", "cleric", "wizard", "warlock"],
        "cha": ["sorcerer", "bard", "cleric", "paladin", "warlock"],
    }
    choice = random.choice(primaries[primary])
    return choice


def random_party_with_matching_primary(primary):
    party_first_class = random_primary_class(primary)
    party_first_sub = random_sub_class(party_first_class)
    party_second_class = random_primary_class(primary)
    party_second_sub = random_sub_class(party_second_class)
    party_third_class = random_primary_class(primary)
    party_third_sub = random_sub_class(party_third_class)

    first = f"{party_first_class} - {party_first_sub}"
    second = f"{party_second_class} - {party_second_sub}"
    third = f"{party_third_class} - {party_third_sub}"
    party = [first, second, third]
    return party


def main():
    pass


if __name__ == "__main__":
    main()
