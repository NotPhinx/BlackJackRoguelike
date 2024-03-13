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

def CountCards(cards):
    listtotal = 0
    for card in cards:
        listtotal += card[0]

    return listtotal 
    
        


# Game Logic
if dealer_total <= 16:
    drawn_card = deck.pop()
    dealer.append(drawn_card)
    print(dealer_total)
    dealer_total = CountCards(dealer)
    print('Dealer Draws a', drawn_card[0], 'of', drawn_card[1])

# See Who Won
if player_total > 21:
    print('Player Busts')
elif dealer_total > 21:
    print('Dealer Busts')
elif player_total > dealer_total:
    print('Player Wins')
elif dealer_total > player_total:
    print('Dealer Wins')
else:
    print('Push')

# Print Totals   
print(player_total, dealer_total)