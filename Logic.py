import random

# Basic Cards
faces = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
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

def split(hand):
    hand1 = [hand[0]]
    hand2 = [hand[1]]

    return hand1, hand2


def CountCards(cards):
    listtotal = 0
    for card in cards:
        if isinstance(card[0], str):  # Check if the card is a face card
            if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King':
                card = (10, card[1])  # Convert face card to (10, suit)
            elif card[0] == 'Ace':
                if(listtotal + 11 > 21):
                    card = (1, card[1])
                else:
                    card = (11, card[1])  # Convert Ace to (11, suit)
        listtotal += card[0]

    return listtotal 

# Game Loop
Playagain = 'Yes'
Split = False

while(Playagain == 'Yes'): 
    playerH1_total = 0
    playerH2_total = 0

    # Print Player and Dealer Cards   
    player_total = CountCards(player)
    dealer_total = CountCards(dealer)  
    print('Player Total:', player_total)
    print('Dealer Total:', dealer_total)


    # Game Logic

    #Player Logic
    while player_total != 21:
        if player_total > 21:
            break
        if player_total == 21:
            break
        if player_total < 21:
            if player[0][0] == player[1][0]:
                split_or_stay = input("Split or Stay? ")
                if split_or_stay == 'Split':
                    Split = True
                    hand1, hand2 = split(player)
                    playerH1_total = CountCards(hand1)
                    playerH2_total = CountCards(hand2)

                    print('Player 1st Hand Total:', playerH1_total)
                    print('Player 2nd Hand Total:', playerH2_total)
                    player_total = CountCards(hand1)
                    print('Player 1st Hand Total:', player_total)
                    hit_or_stay = input("Hit or Stay? ")
                    if hit_or_stay == 'Hit':
                        drawn_card = deck.pop()
                        hand1.append(drawn_card)
                        print(player_total)
                        player_total = CountCards(hand1)
                        print('Player Draws a', drawn_card[0], 'of', drawn_card[1])
                        print('Player 1st Hand Total:', playerH1_total)
                    else:
                        break
                    player_total = CountCards(hand2)
                    hit_or_stay = input("Hit or Stay? ")
                    if hit_or_stay == 'Hit':
                        drawn_card = deck.pop()
                        hand1.append(drawn_card)
                        print(player_total)
                        player_total = CountCards(hand1)
                        print('Player Draws a', drawn_card[0], 'of', drawn_card[1])
                        print('Player 2nd Hand Total:', playerH2_total)
                    else:
                        break
                    print('Player 2nd Hand Total:', player_total)
                    hit_or_stay = input("Hit or Stay? ")
                    if hit_or_stay == 'Hit':
                        drawn_card = deck.pop()
                        hand2.append(drawn_card)
                        print(player_total)
                        player_total = CountCards(hand2)
                        print('Player Draws a', drawn_card[0], 'of', drawn_card[1])
                        print('Player Total:', player_total)
                    else:
                        break
                    break
                else:
                    break
            else:
                hit_or_stay = input("Hit or Stay? ")
                if hit_or_stay == 'Hit':
                    drawn_card = deck.pop()
                    player.append(drawn_card)
                    print(player_total)
                    player_total = CountCards(player)
                    print('Player Draws a', drawn_card[0], 'of', drawn_card[1])
                    print('Player Total:', player_total)
            
                else:
                    break

    #Dealer Logic
    if hit_or_stay == 'Stay':
        while dealer_total <= 16 and dealer_total != 21:
            drawn_card = deck.pop()
            dealer.append(drawn_card) 
            dealer_total = CountCards(dealer)
            print('Dealer Draws a', drawn_card[0], 'of', drawn_card[1])


        print(player_total)




    # See Who Won
    
    if player_total > 21 or playerH1_total > 21 or playerH2_total > 21:
        print('Player Busts')
    elif dealer_total > 21:
        print('Dealer Busts')
    elif player_total == 21 or playerH1_total == 21 or playerH2_total == 21:
        print('Player got BlackJack')
        print('Player Wins')
    elif dealer_total == 21:
        print('Dealer got BlackJack')
        print('Dealer Wins')
    elif player_total > dealer_total or playerH1_total > dealer_total or playerH2_total > dealer_total:
        print('Player Wins')
    elif dealer_total > player_total or dealer_total > playerH1_total or dealer_total > playerH2_total:
            print('Dealer Wins')
    else:
        print('Push')


    # Print Totals
    if Split == True: 
        print('Player 1st Hand Score: ', playerH1_total)
        print('Player 2nd Hand Score: ', playerH2_total)
    else:
        print('Player Score: ', player_total)

    print('Dealer Score: ', dealer_total)

    # Ask to play again
    Playagain = input('Do you want to play again? Yes or No: ')
    if Playagain == 'Yes':
        player = []
        dealer = []
        player.append(deck.pop())
        dealer.append(deck.pop())
        player.append(deck.pop())
        dealer.append(deck.pop())
    else:
        break