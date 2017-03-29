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

class Card:
    '''
        Creates a card with a value and a suit
        Value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        Suit = ['C', 'D', 'H', 'C']
    '''

    # define class variables
    value = None
    suit = None

    # create the card
    def __init__(self, card_value, card_suit):
        self.value = card_value
        self.suit = card_suit

    # return the value of the card as an integer
    def get_value(self):
        if self.value == 'A':
            return 11
        elif self.value in ('K', 'Q', 'J'):
            return 10
        else:
            return int(self.value)

    # print the card
    def print_card(self):
        return (self.value, self.suit)

class Hand:
    '''
        Creates a hand, which is a list of cards having a value, which is a
        summation of all card values
    '''

    # define class variables
    hand = None

    # Create an empty hand
    def __init__(self):
        self.hand = []

    # returns the hand total
    def get_hand_total(self):

        # initialize varaibles
        aces_count = 0
        total = 0

        # loop through the cards in the hand to determine hand total
        for card in self.hand:

            # increase the hand total
            total += card.get_value()

            # count for the number of aces found
            if card.get_value() == 11:
                aces_count += 1

        while total > 21 and aces_count > 1:
            total -= 11
            aces_count-=1

        return total

    # Add a card to your hand
    def deal_card(self, deck):
        self.hand.append(deck.deal())


    # print hand
    def print_hand(self, hide_dealer_hand, name):

        # define variable to hold hand print out
        hand = name + ' has'

        # print each card in the hand
        if hide_dealer_hand:
            hand += ' ' + str(self.hand[0].print_card()) + ' (?, ?)'
        else:
            for card in self.hand:
                hand += ' ' + str(card.print_card())

            # Get hand total
            hand += ' for a total of ' + str(self.get_hand_total())

        print(hand)



class Deck:
    '''
        Creates a deck of 52 cards.  Cards have the following values:
        Value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        Suit = ['C', 'D', 'H', 'C']
    '''

    # define class variables
    deck = []

    # initialize the deck
    def __init__(self):

        # define suits & cards
        suits = ['H', 'D', 'S', 'C']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []

        # loop through the suits & cards to create the cards
        for s in range(0, len(suits)):
            for c in range(0, len(cards)):

                # create the card
                card = Card(cards[c], suits[s])
                print('creating card {0} '.format(card.print_card()))

                # add the card to the deck
                self.deck.append(card)

    def get_total(self):
        return len(self.deck)

    # shuffles the deck
    def shuffle(self):
        # shuffle the deck
        shuffle(self.deck)

    # returns one card from the top of the deck
    def deal(self):
        return self.deck.pop()


class Blackjack_game:
    '''
        Creates a blackjack game with 2 players (a real person and a dealer)
        Rules
        * Get 21 points on the playser first two cards - blackjack
        * Reach a final score higher than the dealer without exceeding 21
        * Let the dealer draw additional cards until their hand exceeds 21
        * Dealer hits until cards total 17 or more
        * Dealer hits on soft 17
    '''
    deck = None
    player_hand = None
    dealer_hand = None


    # initalize the game
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        print('--------------------')
        print('Welcome To Blackjack')
        print('--------------------\n')

        self.play_game()


    def play_game(self):

        print('Dealing Hands ...\n')

        # deal the Hands
        self.deal_hands()

        #print the Hands
        self.player_hand.print_hand(False, 'Player')
        self.dealer_hand.print_hand(True, 'Dealer')

        #print
        player_response = input.('Player, would you like to (H)it or (S)tand?')


    def deal_hands(self):
        self.player_hand.deal_card(self.deck)
        self.dealer_hand.deal_card(self.deck)
        self.player_hand.deal_card(self.deck)
        self.dealer_hand.deal_card(self.deck)


# class Blackjack:
#     '''
#         Creates a blackjack game, managing the creation of a deck, dealing of cards
#         and calculating win/loss
#     '''
#     __deck = []
#     __dealer_hand = []
#     __dealer_total = 0
#     __player_hand = []
#     __player_total = 0
#     __has_winner = False
#
#     def __init__(self):
#
#         # create the deck
#         self.create_deck()
#
#         # deal the hands
#         self.deal_hands()
#
#         # calculate hand totals
#         self.__dealer_total = self.calculate_total(self.__dealer_hand)
#         self.__player_total = self.calculate_total(self.__player_hand)
#
#         # set hand_status to be True, meaning a hand is in progress
#         self.__hand_status = True
#
#     def create_deck(self):
#         '''
#             Initializes the deck of cards. Each card is represented by a tuple defined by (card number, suit).
#             The deck of cards will be shuffled randomly
#         '''
#
#         # define suits & cards
#         suits = ['H', 'D', 'S', 'C']
#         cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#
#         # loop through the suits & cards to create the cards
#         for s in range(0, len(suits)):
#             for c in range(0, len(cards)):
#                 card = (cards[c], suits[s])
#                 # add the card to the deck
#                 self.__deck.append(card)
#
#         # shuffle the deck
#         shuffle(self.__deck)
#
#     def deal_hands(self):
#         '''
#             Initializes the player & dealer hands
#         '''
#         # Deal the hands
#         self.__player_hand.append(self.__deck.pop())
#         self.__dealer_hand.append(self.__deck.pop())
#         self.__player_hand.append(self.__deck.pop())
#         self.__dealer_hand.append(self.__deck.pop())
#
#     def calculate_total(self, hand):
#         '''
#             Returns the total
#         '''
#
#         total = 0
#         aces_count = 0
#
#         # loop through the cards in the hand to determine hand total
#         for card, suit in hand:
#             if card in ('J', 'Q', 'K'):
#                 total+= 10
#             elif card == 'A':
#                 total+= 11
#                 aces_count+= 1
#             else:
#                 total += int(card)
#
#         while total > 21 and aces_count > 1:
#             total -= 11
#             aces_count-=1
#
#         return total
#
#     def has_winner(self):
#         return self.__has_winner
#
#     def status(self):
#         return self.__status

#    def print_hands(self):
        #if player_total == 21

# ----------------------------------------------------------------------------
# Main program
#
# ----------------------------------------------------------------------------

# def get_play_again():
#     while True:
#         play_again = input('would you like to play again (y/n)')
#
#         if play_again == 'y':
#             return True
#         elif play_again == 'n':
#             return False
#         else:
#             print('sorry, I did not understand your response')

blackjack = Blackjack_game()



#print('\n')
#print('Your hand: {0[0][0]}{0[0][1]}, {0[1][0]}{0[1][1]}'.format(player_hand))
#print('Dealer hand: ?, {0[1][0]}{0[1][1]}\n'.format(dealer_hand))
