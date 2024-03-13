import random

# Basic Cards
faces = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# Basic Deck
deck = []

# Generate Basic Deck of Cards
for suit in suits:
    for face in faces:
        deck.append((face, suit))

print(deck)