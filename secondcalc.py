import random
import collections

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        # Create a list of all 52 cards in a standard deck
        self.cards = [Card(rank, suit) for rank in range(2, 14) for suit in ('hearts', 'diamonds', 'spades', 'clubs')]

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
        if self.suit == "h":
             suit = "hearts"
        if self.suit == "s":
             suit = "spades"
        if self.suit == "d":
             suit = "diamonds"
        if self.suit == "c":
             suit = "clubs"

    def __repr__(self):
        if self.rank == 11:
             return f"Jack of {self.suit}"
        if self.rank == 12:
             return f"Queen of {self.suit}"
        if self.rank == 13:
             return f"King of {self.suit}"
        if self.rank == 14:
             return f"Ace of {self.suit}"
        else:
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
        self.deck = deck
        self.community_cards = []

    def deal_flop(self):
        self.community_cards.extend(self.deck.deal_card() for _ in range(3))

    def deal_turn(self):
        self.community_cards.append(self.deck.deal_card())

    def deal_river(self):
        self.community_cards.append(self.deck.deal_card())

hearts = [Card(1, 'hearts'), Card(2, 'hearts'), Card(3, 'hearts'), Card(4, 'hearts'), Card(5, 'hearts'), Card(6, 'hearts'), Card(7, 'hearts'), Card(8, 'hearts')]
spades = [Card(1, 'spades'), Card(2, 'spades'), Card(3, 'spades'), Card(4, 'spades'), Card(5, 'spades'), Card(6, 'spades'), Card(7, 'spades'), Card(8, 'spades')]
clubs = [Card(1, 'clubs'), Card(2, 'clubs'), Card(3, 'clubs'), Card(4, 'clubs'), Card(5, 'clubs'), Card(6, 'clubs'), Card(7, 'clubs'), Card(8, 'clubs')]
diamonds = [Card(1, 'diamonds'), Card(2, 'diamonds'), Card(3, 'diamonds'), Card(4, 'diamonds'), Card(5, 'diamonds'), Card(6, 'diamonds'), Card(7, 'diamonds')]

ones = [Card(1,'diamonds'), Card(1,'clubs'), Card(1,'hearts'), Card(1,'spades')]
twos = [Card(2,'diamonds'), Card(2,'clubs'), Card(2,'hearts'), Card(2,'spades')]
threes = [Card(3,'diamonds'), Card(3,'clubs'), Card(3,'hearts'), Card(3,'spades')]
fours = [Card(4,'diamonds'), Card(4,'clubs'), Card(4,'hearts'), Card(4,'spades')]
fives = [Card(5,'diamonds'), Card(5,'clubs'), Card(5,'hearts'), Card(5,'spades')]
sixes = [Card(6,'diamonds'), Card(6,'clubs'), Card(6,'hearts'), Card(6,'spades')]
sevens = [Card(7,'diamonds'), Card(7,'clubs'), Card(7,'hearts'), Card(7,'spades')]
eights = [Card(8,'diamonds'), Card(8,'clubs'), Card(8,'hearts'), Card(8,'spades')]
nines = [Card(9,'diamonds'), Card(9,'clubs'), Card(9,'hearts'), Card(9,'spades')]
tens = [Card(10,'diamonds'), Card(10,'clubs'), Card(10,'hearts'), Card(10,'spades')]
elevens = [Card(11,'diamonds'), Card(11,'clubs'), Card(11,'hearts'), Card(11,'spades')]
twelves = [Card(12,'diamonds'), Card(12,'clubs'), Card(12,'hearts'), Card(12,'spades')]
thirteens = [Card(13,'diamonds'), Card(13,'clubs'), Card(13,'hearts'), Card(13,'spades')]
fourteens = [Card(14,'diamonds'), Card(14,'clubs'), Card(14,'hearts'), Card(14,'spades')]

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

def calculate_odds(hand, community_cards, target_card):
    known_combined = hand + community_cards
    known_cards = []
    for card in known_combined:
         known_cards.append([card.rank, card.suit])

    final = 1 / (52 - len(known_cards))
    target = [target_card.rank, target_card.suit]
    if target in known_cards:
         final = 0
   # rank_counts = collections.Counter([card.rank for card in known_cards])
   # suit_counts = collections.Counter([card.suit for card in known_cards])
    return(final)

def multiple_odds(hand, community_cards, target_cards):
    total = []
    if isinstance(target_cards, list):
         for target_card in target_cards:
              one = calculate_odds(hand, community_cards, target_card)
              total.append(one)
              any = sum(total)
         return any
    return calculate_odds(hand, community_cards, target_cards)

def looking_for():
    want_rank = input("What rank are you looking for: ")
    want_suit = input("What suit are you looking for: ")
    if want_suit == "all":
         return [Card(int(want_rank), "clubs"), Card(int(want_rank), "diamonds"), Card(int(want_rank), "spades"), Card(int(want_rank), "hearts")]
    if want_suit == "h":
         want_suit = "hearts"
    if want_suit == "s":
         want_suit = "spades"
    if want_suit == "d":
         want_suit = "diamonds"
    if want_suit == "c":
         want_suit = "clubs"
    if want_rank == "all":
          return [Card(1, want_suit), Card(2, want_suit), Card(3, want_suit), Card(4, want_suit), Card(5, want_suit), Card(6, want_suit), Card(7, want_suit), Card(8, want_suit), Card(9, want_suit), Card(10, want_suit), Card(11, want_suit), Card(12, want_suit), Card(13, want_suit), Card(14, want_suit)]

    intention = Card(int(want_rank), want_suit)
    return intention

def looking_for_multiple():
    how_many = int(input("How many iterations: "))
    inc = 0
    all = []
    while inc < how_many:
         answer = looking_for()
         all.append(answer)
         inc += 1
    return all


inc = -1
while inc < 0:
    inc+=1
    # Create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()
    # Create three players
    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Charlie")
   
    TexasHoldemGame.deck = deck
    # Deal two cards to each player
    for _ in range(2):
        player1.draw_card(deck.deal_card())
        player2.draw_card(deck.deal_card())
        player3.draw_card(deck.deal_card())
    
    start = TexasHoldemGame([player1, player2, player3])
    start.deal_flop()

    in_hand = player1.hand
    on_board = start.community_cards

    print("You have " + str(in_hand) + " in your hand.")
    print("The cards " + str(on_board) + " are on the table")
    
    want = looking_for_multiple()
    for item in want:
        test = multiple_odds(in_hand, on_board, item)
        print(test)

    start.deal_turn()
    print(start.community_cards[3])
    start.deal_river()
    print(start.community_cards[4])


