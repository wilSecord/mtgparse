import scrython as sf
import re


def print_text_and_name(name: str) -> list[str]:
    card = sf.cards.Named(fuzzy=name)
    try:
        o_text = card.oracle_text()
    except KeyError:
        for item in card.card_faces():
            if item["name"] == name:
                o_text = item["oracle_text"]

    lines = o_text.split("\n")
    for item in lines:
        if ':' in item:
            cost = re.split(': ', item)[0]
            return cost.split(', ')


print(print_text_and_name("Elesh Norn"))
