import random

class Card:
	def __init__(self, number, suit):
		#each card gets a number, face cards are converted to numbers
		converted_number = number
		face = ['j','J','q','Q','k','K','a','A']
		face_to_number = [11, 11, 12, 12, 13, 13, 14, 14]
		numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
		if number in face:
			converted_number = face_to_number[face.index(number)]
		if converted_number not in numbers:
			print("Error: Invalid number")
			exit()
		self.number = converted_number

		#each card gets a suit
		suits = ['S','C','H','D']
		if suit.upper() not in suits:
			print("Error: Invalid suit")
			exit()
		self.suit = suit.upper()

#deck of all 52 cards is created, not shuffled
deck = []
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['S','C','H','D']
for n in numbers:
	for s in suits:
		card = Card(n, s)
		deck.append(card)


def distribute(players, deck=deck):
	#deck is shuffled
	random.shuffle(deck)
	hands = []
	board = []
	#each player is given two cards from the top of the deck, card are removed from deck
	for player in range(0, players):
		hand = [str(deck[0].number)+deck[0].suit, str(deck[1].number)+deck[1].suit]
		deck.pop(0) and deck.pop(1)
		hands.append(hand)
	#lays out the five cards to be put down for texas hold em
	for n in range(0, 5):
		board.append(str(deck[0].number)+deck[0].suit)
		deck.pop(0)
	return [hands, board, deck]

#is there a pair in a given list
def pair(hand):
	revised_hand = []
	inc = 0
	result = []
	for n in hand:
		add = n[:-1]
		revised_hand.append(add)
	while len(revised_hand) > 0:
		now = revised_hand[0]
		revised_hand.pop(0)
		for k in revised_hand:
			if now==k:
				result.append(now)
				break
	if len(result) == 0:
		result = False
	return result

#differtiates between pair in hand, on board, and between
def is_pair(board, hand):
	print(board, hand)
	pair_on_board = pair(board)
	pair_in_hand = pair(hand)
	both = board + hand
	pair_between = pair(both)
	print(pair_between)
	#makes sure pair between is only found between
	#if isinstance(pair_between, list):
	#	if isinstance(pair_on_board, list):
	#		pair_between = [i for i in pair_between if i not in pair_on_board]
	#	if isinstance(pair_in_hand, list):
	#		pair_between = [i for i in pair_between if i not in pair_in_hand]
	#	if len(pair_between) == 0:
	#		pair_between = False
	return [pair_in_hand, pair_on_board, pair_between]

def comp_pairs(board, hand):
	use = is_pair(board, hand)
	pairs_in_hand = [False]
	pairs_on_board = [False, False, False]
	pairs_between = []
	if use[1] is not False:
		pairs_on_board = pairs_on_board_func(board)
	return pairs_on_board

def pairs_on_board_func(board):
	pairs_on_board = [False, False, False]
	use = is_pair(board, ['10s', '10c'])
	if len(use[1]) > 2:
		#finds if there is a four pair on the board
		if use[1][0] == use[1][1] and use[1][1] == use[1][2]:
			four_pair = use[1][0]
			pairs_on_board[2] = four_pair
		#finds if there is a full house on the board
		else:
			if use[1][0] == use[1][1]:
				three_pair = use[1][0]
				two_pair = use[1][2]
			else: 
				three_pair = use[1][2]
				two_pair = [i for i in use[1] if i is not three_pair]
			pairs_on_board[1] = three_pair
			pairs_on_board[0] = two_pair[0]
	#finds if there is a three pair (not full house) on the board
	if len(use[1]) > 1:
		if use[1][0] == use[1][1]:
			three_pair = use[1][0]
		else:
			pairs_on_board[0] = [use[1][0], use[1][1]]
	return pairs_on_board


go = distribute(4)
print(comp_pairs(go[1], go[0][0]))

#now = Hands(go[1], go[0][0])
#print(now.is_pair)
