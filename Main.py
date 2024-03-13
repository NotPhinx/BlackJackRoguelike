import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value} of {self.suit}"
    

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

deck = Deck()
deck.shuffle()
card = deck.draw()
print(card)
