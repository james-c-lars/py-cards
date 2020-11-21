import cards as c
import os

def clear():
	os.system('clear')

class TableauColumn(c.Deck):

	def __init__(self, cards=[]):
		self.cards = list(cards)

	def __repr__(self):
		return '<TableauColumn cards:' + str(self.cards) + '>'

	def add(self, card):
		self.cards.append(card)
	def draw(self, num=1):
		start_index = len(self)-num

		if start_index != 0:
			self[start_index - 1].flip_face_up()

		return c.Deck([self.cards.pop(start_index) for i in range(start_index, len(self))])

	def flip_bottom(self):
		self[-1].flip_face_up()
	def can_place(self, card):
		if len(self) == 0:
			return card.eq_number('King')

		return card.color != self[-1].color and int(card) == int(self[-1]) - 1

	def place(self, cards):
		self.cards += cards


class Tableau():
	MAX_CARD_STR = 17

	def __init__(self, deck, col_count=7):
		self.cols = [TableauColumn() for i in range(col_count)]

		deck.shuffle()
		deck.flip_face_down()
		for i in range(col_count):
			deck.deal(piles=self[i:], card_count=1)
		deck.flip_face_up()

		for col in self.cols:
			col.flip_bottom()

	def __str__(self):
		max_col = max([len(col) for col in self])

		return_string = ''
		for i in range(max_col):
			for col in self:
				if len(col) > i:
					return_string += str(col[i]) + (' ' * (Tableau.MAX_CARD_STR - len(str(col[i])))) + '|'
				else:
					return_string += ' ' * (Tableau.MAX_CARD_STR) + '|'

			return_string += '\n'

		return return_string

	def __repr__(self):
		return '<Tableau cols:' + str(self.cols) + '>'

	def __len__(self):
		return len(self.cols)
	def __iter__(self):
		return iter(self.cols)
	def __getitem__(self, item):
		return self.cols[item]


class Foundation(c.Deck):

	def __init__(self, cards=[]):
		self.cards = list(cards)

	def __str__(self):
		if len(self) > 0:
			return str(self.cards[-1])
		return 'Empty'
	def __repr__(self):
		return '<Foundation cards:' + str(self.cards) + '>'

	def full(self):
		return len(self) == 13
	def suit(self):
		if len(self) > 0:
			return self[0].suit
		return None
	def can_place(self, card):
		if len(self) == 0:
			return int(card) == 1
		return card.suit == self.suit() and int(card) == int(self[-1]) + 1
	def place(self, cards):
		assert len(cards) == 1, cards
		self.cards.append(cards[0])


class Talon(c.Deck):

	def __str__(self):
		if len(self.cards) > 0:
			return str(self.cards[-1])
		return 'Empty       '
	def __repr__(self):
		return '<Discard' + c.Deck.__repr__()[5:]

	def add(self, card):
		self.cards.append(card)

	def draw(self, num=1):
		return [self.cards.pop(-1)]


class Table():

	def __init__(self):
		self.deck = c.Deck(fill=True)
		self.tableau = Tableau(self.deck)
		self.foundations = [Foundation() for i in range(4)]
		self.talon = Talon()

	def __str__(self):
		string = 'Deck: (Face Down)|' if len(self.deck) > 0 else 'Deck: Empty      |'
		string += 'Talon: ' + str(self.talon)
		string += ' ' * ((Tableau.MAX_CARD_STR + 1) - 1 - len(string) % (Tableau.MAX_CARD_STR + 1)) + '|'
		for f in self.foundations:
			string += str(f)
			string += ' ' * ((Tableau.MAX_CARD_STR) - len(string) % (Tableau.MAX_CARD_STR + 1)) + '|'
		string += '\n\n'
		string += str(self.tableau) + '\n\n'

		return string





clear()

print('Welcome to Big Solitaire!')
print('Your goal is to fill the four foundations with cards from each suit')
print('You must start with an ace and then add cards one higher on top')

print('\nTo flip over a card onto the talon, enter 0 twice')
print('Once to show that you want to move a card to the talon')
print('Twice to show that you want to flip a new card on top of the talon')

print('\nIf you enter an invalid move (like taking 4 cards from a column with only 3)')
print('nothing will happen and you will be prompted again to choose what to do')

input('\nPress enter to begin...')


t = Table()

while not all([f.full() for f in t.foundations]):
	clear()
	print(t)

	# Which pile will they take from?
	take_select = None
	while take_select == None:
		try:
			take_select = int(input('0: Talon, 1-7: Tableau columns\nFrom what pile will you move cards: '))
		except ValueError:
			print('ValueError')
			continue

		if take_select > 7 or take_select < 0:
			print('Invalid choice')
			take_select = None

	# How many cards will they take?
	if take_select == 0:
		if len(t.talon) == 0:
			t.talon.add(t.deck.draw())
			continue

		number_select = None
		while number_select == None:
			try:
				number_select = int(input('Enter the number of cards you\'ll move: '))
			except ValueError:
				print('ValueError')
				continue

			if number_select < 0 or number_select > 1:
				print('Invalid choice')
				number_select = None

		if number_select == 0:
			if len(t.deck) == 0:
				t.deck += t.talon
				t.deck.shuffle()

			t.talon.add(t.deck.draw())
			continue

		card_to_move = t.talon[-1]
		number_select = 1
		take_pile = t.talon
	else:
		print()

		number_select = None
		while number_select == None:
			try:
				number_select = int(input('Enter the number of cards you\'ll move: '))
			except ValueError:
				print('ValueError')
				continue

			if number_select < 1:
				print('Invalid choice')
				number_select = None

			if number_select:
				try:
					take_pile = t.tableau[take_select-1]
					card_to_move = take_pile[len(take_pile) - number_select]
				except IndexError:
					print('IndexError')
					number_select = None

				if card_to_move and not card_to_move.face_one_up:
					print('Invalid choice')
					number_select = None

	print()

	# Where will they move the cards?
	place_select = None
	while place_select == None:
		try:
			place_select = int(input('0: Foundation, 1-7: Tableau columns\nWhere will you move cards: '))
		except ValueError:
			print('ValueError')
			continue

		if place_select == 0 and number_select != 1:
			print('Too many cards')
			place_select = None

		if place_select < 0 or place_select > 7:
			print('Invalid choice')
			place_select = None


	# Resolving their choices
	if place_select == 0:
		for f in t.foundations:
			if f.can_place(card_to_move):
				f.place(take_pile.draw())
				break
	else:
		place_pile = t.tableau[place_select-1]
		if place_pile.can_place(card_to_move):
			place_pile.place(take_pile.draw(number_select))


clear()
print(t)

print('You\'ve won! Nice job!')