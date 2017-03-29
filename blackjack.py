# ------------------------- #
# Blackjack in python       #
# ------------------------- #
#

# Background
# ==========
#
# Project Description
# ====================
# Create a blackjack simulation using python
#
# Rules
# Get 21 points on the playser first two cards - blackjack
# Reach a final score higher than the dealer without exceeding 21
# Let the dealer draw additional cards until their hand exceeds 21
# Dealer hits until cards total 17 or more
# Dealer hits on soft 17
# -----------------------------------------------------------------------------
from random import shuffle

class Blackjack:
    '''
        Creates a blackjack game, managing the creation of a deck, dealing of cards
        and calculating win/loss
    '''
    __deck = []
    __dealer_hand = []
    __dealer_total = 0
    __player_hand = []
    __player_total = 0

    def __init__(self):

        # create the deck
        self.create_deck()

        # deal the hands
        self.deal_hands()

        # calculate hand totals
        self.__dealer_total = self.calculate_total(self.__dealer_hand)
        self.__player_total = self.calculate_total(self.__player_hand)


    def create_deck(self):
        '''
            Initializes the deck of cards. Each card is represented by a tuple defined by (card number, suit).
            The deck of cards will be shuffled randomly
        '''

        # define suits & cards
        suits = ['H', 'D', 'S', 'C']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # loop through the suits & cards to create the cards
        for s in range(0, len(suits)):
            for c in range(0, len(cards)):
                card = (cards[c], suits[s])
                # add the card to the deck
                self.__deck.append(card)

        # shuffle the deck
        shuffle(self.__deck)

    def deal_hands(self):
        '''
            Initializes the player & dealer hands
        '''
        # Deal the hands
        self.__player_hand.append(self.__deck.pop())
        self.__dealer_hand.append(self.__deck.pop())
        self.__player_hand.append(self.__deck.pop())
        self.__dealer_hand.append(self.__deck.pop())

    def calculate_total(self, hand):
        '''
            Returns the total
        '''

        total = 0
        aces_count = 0

        # loop through the cards in the hand to determine hand total
        for card, suit in hand:
            if card in ('J', 'Q', 'K'):
                total+= 10
            elif card == 'A':
                total+= 11
                aces_count+= 1
            else:
                total += int(card)

        while total > 21 and aces_count > 1:
            total -= 11
            aces_count-=1

        return total


#    def hit(self):

#    def stand(self):

#    def print_hands(self):


# ----------------------------------------------------------------------------
# Main program
#
# ----------------------------------------------------------------------------

blackjack = Blackjack()




#print('\n')
#print('Your hand: {0[0][0]}{0[0][1]}, {0[1][0]}{0[1][1]}'.format(player_hand))
#print('Dealer hand: ?, {0[1][0]}{0[1][1]}\n'.format(dealer_hand))
