import random

# Basic Cards
faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
deck = []

# Generate Basic Deck of Cards
for suit in suits:
    for face in faces:
        deck.append((face, suit))

# Shuffle Newly Created Deck
random.shuffle(deck)

# Hands for player and dealer
player = []
dealer = []

# Deal Cards
player.append(deck.pop())
dealer.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())

player_total = (player[0][0] + player[1][0])
dealer_total = (dealer[0][0] + dealer[1][0])

# Game Logic
if dealer_total <= 16:
    drawn_card = deck.pop()
    dealer.append(drawn_card)
    dealer_total = ()
    print('Dealer Draws a', drawn_card[0], 'of', drawn_card[1])

# See Who Won   

print(player_total, dealer_total)