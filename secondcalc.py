import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        # Create a list of all 52 cards in a standard deck
        self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in ('hearts', 'diamonds', 'spades', 'clubs')]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def print_deck(self):
        for card in self.cards:
            print(card)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

    def fold(self):
        self.hand = []

    def show_hand(self):
        return self.hand

class TexasHoldemGame:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []

    def deal_flop(self):
        self.community_cards.extend(self.deck.deal_card() for _ in range(3))

    def deal_turn(self):
        self.community_cards.append(self.deck.deal_card())

    def deal_river(self):
        self.community_cards.append(self.deck.deal_card())

def is_pair(hand):
    ranks = [card.rank for card in hand]
    return len([rank for rank in set(ranks) if ranks.count(rank) == 2]) > 0

def is_three_of_a_kind(hand):
    ranks = [card.rank for card in hand]
    return len([rank for rank in set(ranks) if ranks.count(rank) == 3]) > 0

def is_straight(community_cards, hand):
    cards = community_cards + hand
    ranks = sorted([card.rank for card in cards], reverse=True)
    for i in range(len(ranks) - 1):
        if ranks[i] - ranks[i + 1] != 1:
            return False
    return True

def is_flush(hand):
    suits = [card.suit for card in hand]
    return len(set(suits)) == 1


inc = 0
while inc < 1000:
    inc+=1
    # Create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()

    # Create three players
    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Charlie")

    # Deal two cards to each player
    for _ in range(2):
        player1.draw_card(deck.deal_card())
        player2.draw_card(deck.deal_card())
        player3.draw_card(deck.deal_card())

    start = TexasHoldemGame([player1, player2, player3])
    start.deal_flop()
    start.deal_turn()
    start.deal_river()

    if (is_flush(start.community_cards)):
        print("good")



