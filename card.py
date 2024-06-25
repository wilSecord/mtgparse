import scrython as sf
import re

class Card:
    def __init__(self, search: str) -> None:
        self.sf_card = sf.cards.Named(exact=search)
        self.otext: dict[str, list] = {'face1': [], 'face2': []}
        self.statics: dict[str, list] = {'face1': [], 'face2': []}
        self.activateds: dict[str, list] = {'face1': [], 'face2': []}
        self.triggereds: dict[str, list] = {'face1': [], 'face2': []}
        self.chapters: dict[str, list] = {'face1': [], 'face2': []}
        self.get_otext()
        self.get_abilities()

    def get_abilities(self):
        for face, otext in self.otext.items():
            for item in otext:
                if ':' in item:
                    self.activateds[face].append(item)
                elif re.match(r'(Whenever|When|As)', item) != None:
                    self.triggereds[face].append(item)
                elif re.match(r'^(IX|IV|V?I{0,3})(\s-\s|, )', item) != None:
                    self.chapters[face].append(item)
                else:
                    for jtem in item.split(', '):
                        if jtem in sf.KeywordAbilities().data():
                            self.statics[face] = item.split(', ')

    def get_otext(self):
        try:
            self.otext['face1'] = (self.sf_card.oracle_text().split('\n'))
        except KeyError:
            self.otext['face1'] = (self.sf_card.card_faces()[0]['oracle_text'].split('\n'))
            self.otext['face2'] = (self.sf_card.card_faces()[1]['oracle_text'].split('\n'))
        for k, v in self.otext.items():
            for i in range(len(v)):
                self.otext[k][i] = self.otext[k][i].replace('—', '-')


card = Card('Elesh Norn')
print(card.otext)
print(card.statics)
print(card.activateds)
print(card.triggereds)
print(card.chapters)
