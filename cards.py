"""
Used to create and manipulate playing cards as well as data structures associated with them.
"""

from random import shuffle, choice



class Card():
	"""
	Represents a generic card with two sides which can be flipped to show one side at a time.

	Attributes:
		face_one (str): What is on the first face of the card.
		face_two (str): What is on the second face of the card.
		face_one_up (bool): Whether the first face is the one that is flipped up.
	"""


	FACE_DOWN = '(Face Down)'

	def __init__(self, face_one, face_two=FACE_DOWN, face_one_up=True):
		self.face_one = face_one
		self.face_two = face_two
		self.face_one_up = face_one_up
		
	def flip(self):
		"""Reverse which face is flipped up."""
		self.face_one_up = not self.face_one_up
	def flip_face_up(self):
		"""Turn face one up."""
		self.face_one_up = True
	def flip_face_down(self):
		"""Turn face two up."""
		self.face_one_up = False
	def flip_card(self, turned_up):
		"""self.face_one_up = turned_up"""
		self.face_one_up = turned_up
	def eq_face_one(self, other):
		"""Return face_one == other"""
		return face_one == other
	def eq_face_two(self, other):
		"""Return face_two == other"""
		return face_two == other
	def copy(self):
		"""Return a copy of the card."""
		return Card(self.face_one.copy(), self.face_two.copy(), self.face_one_up)

	def __str__(self):
		return str(self.face_one) if self.face_one_up else str(self.face_two)
	def __repr__(self):
		return '<Card face_one:' + str(self.face_one) + ', face_two:' + str(self.face_two) + ', face_one_up:' + str(self.face_one_up) + '>'

	# Performed on the turned up face
	def __eq__(self, other):
		return str(self) == str(other)
	def __ne__(self, other):
		return str(self) != str(other)
	def __hash__(self):
		return hash((self.face_one, self.face_two, self.face_one_up))


class Number():
	"""
	Represents the number or face of a playing card.

	Attributes:
		name (str): String representation of the Number
		num (int): Integer representation of the Number
	"""

	def __init__(self, new_num):
		number = str(new_num).upper()
		
		if number in {"ACE", "ONE", "1", "A"}:
			self.name = "Ace"
			self.num = 1
		elif number in {"TWO", "2"}:
			self.name = "Two"
			self.num = 2
		elif number in {"THREE", "3"}:
			self.name = "Three"
			self.num = 3
		elif number in {"FOUR", "4"}:
			self.name = "Four"
			self.num = 4
		elif number in {"FIVE", "5"}:
			self.name = "Five"
			self.num = 5
		elif number in {"SIX", "6"}:
			self.name = "Six"
			self.num = 6
		elif number in {"SEVEN", "7"}:
			self.name = "Seven"
			self.num = 7
		elif number in {"EIGHT", "8"}:
			self.name = "Eight"
			self.num = 8
		elif number in {"NINE", "9"}:
			self.name = "Nine"
			self.num = 9
		elif number in {"TEN", "10"}:
			self.name = "Ten"
			self.num = 10
		elif number in {"JACK", "ELEVEN", "11", "J"}:
			self.name = "Jack"
			self.num = 11
		elif number in {"QUEEN", "TWELVE", "12", "Q"}:
			self.name = "Queen"
			self.num = 12
		elif number in {"KING", "THIRTEEN", "13", "K"}:
			self.name = "King"
			self.num = 13
		elif number in {"JOKER", "FOURTEEN", "ZERO", "14", "0"}:
			self.name = "Joker"
			self.num = 0
		else:
			raise ValueError('Number can\'t be created from', new_num)

	def is_face_card(self):
		"""Returns whether the number is a face card."""
		return int(self) > 10
	def copy(self):
		"""Returns a copy of the Number."""
		return Number(self)

	def __str__(self):
		return self.name
	def __int__(self):
		"""Return int(self)."""
		return self.num
	def __repr__(self):
		return '<Number name:' + str(self.name) + ', num:' + str(self.num) + '>'

	def __eq__(self, other):
		return int(self) == int(Number(other))
	def __ne__(self, other):
		return int(self) != int(Number(other))
	def __le__(self, other):
		return int(self) <= int(Number(other))
	def __lt__(self, other):
		return int(self) < int(Number(other))
	def __gt__(self, other):
		return int(self) > int(Number(other))
	def __ge__(self, other):
		return int(self) >= int(Number(other))
	def __add__(self, other):
		"""
		If other is a Suit or str, return a string representing the combination of number and suit.
		Else, return int(self) + int(other).
		"""
		if isinstance(other, (Suit, str)):
			return str(self) + ' of ' + str(Suit(other)) + 's'
		return int(self) + int(other)
	def __hash__(self):
		return hash(int(self))


class Suit():
	"""
	Represents the suit of a playing card.

	Attributes:
		suit (str): String repreesntation of the Suit.
		num (int): Integer representation of the Suit.
	"""

	def __init__(self, new_suit):
		suit = str(new_suit).upper()
		
		if suit in {"HEART", "HEARTS", "0", "ZERO", "H"}:
			self.suit = "Heart"
			self.num = 0
		elif suit in {"CLUB", "CLUBS", "1", "ONE", "C"}:
			self.suit = "Club"
			self.num = 1
		elif suit in {"DIAMOND", "DIAMONDS", "2", "TWO", "D"}:
			self.suit = "Diamond"
			self.num = 2
		elif suit in {"SPADE", "SPADES", "3", "THREE", "S"}:
			self.suit = "Spade"
			self.num = 3
		else:
			raise ValueError('Suit can\'t be created from',new_suit)

	def get_color(self):
		"""Return the color (str) associated with this suit."""
		if int(self)%2 == 0:
			return 'Red'
		return 'Black'
	def copy(self):
		"""Return a copy of this suit."""
		return Suit(self)

	def __str__(self):
		return self.suit
	def __int__(self):
		"""Return int(self)."""
		return self.num
	def __repr__(self):
		return '<Number suit:' + str(self.suit) + ', num:' + str(self.num) + \
			   ', color:' + str(self.get_color()) + '>'

	def __eq__(self, other):
		return int(self) == int(Suit(other))
	def __ne__(self, other):
		return int(self) != int(Suit(other))
	def __add__(self, other):
		return str(Number(other)) + ' of ' + str(self) + 's'
	def __hash__(self):
		return hash(int(self))


class PlayingCard(Card):
	"""
	Represents a playing card with an associated number and suit.

	Attributes:
		number (Number): The number on the playing card.
		suit (Suit): The suit of the playing card.
		color (str): The color of the playing card.
	"""

	@classmethod
	def parse(cls, string):
		"""
		Return a PlayingCard based on parsing string.
		string is expected to be in the form 'number of suit'.
		"""
		words = string.split(sep=' of ')
		if len(words) != 2:
			raise ValueError('When using parse to create PlayingCard, string must be in form "number of suit".')
		return cls(words[0], words[1])

	def __init__(self, number='Ace', suit='Spade', face_one_up=True):
		self.number = Number(number)
		self.suit = Suit(suit)
		self.color = self.suit.get_color()
		
		if str(self.number) == "Joker":
			Card.__init__(self, str(self.number), face_one_up=face_one_up)
		else:
			Card.__init__(self, self.number + self.suit, face_one_up=face_one_up)

	def __int__(self):
		"""Return int(self)."""
		return int(self.number)
	def __repr__(self):
		return '<PlayingCard number:' + str(self.number) + ', suit:' + str(self.suit) + ', color:' + str(self.color) + '>'

	def eq_number(self, other):
		"""Return self.number == Number(other)."""
		return Number(other) == self.number
	def eq_suit(self, other):
		"""Return self.suit == Suit(other)."""
		return self.suit == Suit(other)
	def eq_color(self, other):
		"""Return self.color == other."""
		return self.color == other
	def is_face_card(self):
		"""Return whether this PlayingCard is a face card."""
		return self.number.is_face_card()
	def copy(self):
		"""Return a copy of this PlayingCard."""
		return PlayingCard(self.number.copy(), self.suit.copy(), self.face_one_up)

	def __le__(self, other):
		return int(self) <= int(other)
	def __lt__(self, other):
		return int(self) < int(other)
	def __gt__(self, other):
		return int(self) > int(other)
	def __ge__(self, other):
		return int(self) >= int(other)
	def __add__(self, other):
		"""Return int(self) + int(other)."""
		return int(self) + int(other)


class Pile:

	def __init__(self, cards=set()):
		self.cards = set(cards)

	def __str__(self):
		return str({str(card) for card in self})
	def __repr__(self):
		return '<Pile cards:' + str(self.cards) + '>'
	
	def add(self, card):
		self.cards.add(card)
	def remove(self, card):
		self.cards.remove(card)
		return card
	def empty(self):
		temp = self.cards.copy()
		self.cards.clear()
		return temp
	def flip(self):
		for card in self:
			card.flip()
	def flip_face_up(self):
		for card in self:
			card.flip_face_up()
	def flip_face_down(self):
		for card in self:
			card.flip_face_down()
	def flip_cards(self, up_or_down):
		for card in self:
			card.flip_card(up_or_down)
	def random_card(self):
		return choice(list(self.cards))
	def copy(self):
		cls = type(self)
		return cls([card.copy() for card in self])

	def __len__(self):
		return len(self.cards)
	def __contains__(self, key):
		return key in self.cards
	def __iter__(self):
		return iter(self.cards)

	def __add__(self, other):
		cls = type(self)

		if isinstance(other, Pile):
			return cls(list(self.empty()) + list(other.empty()))

		added = cls(list(self.empty()) + list(other))
		other.clear()

		return added

	def __iadd__(self, other):
		cards_type = type(self.cards)

		if isinstance(other, Pile):
			self.cards = cards_type(list(self.cards) + list(other.empty()))
		else:
			self.cards = cards_type(list(self.cards) + list(other))
			other.clear()

		return self
		
	def __sub__(self, other):
		cls = type(self)

		new_pile = cls([self.remove(card) for card in other if card in self])

		for card in new_pile:
			other.remove(card)

		return new_pile


class Deck(Pile):
	
	def __init__(self, cards=[], fill=False, **kwargs):
		self.cards = list(cards)

		if fill:
			self._fill_deck(**kwargs)

	def __str__(self):
		return str([str(card) for card in self])
	def __repr__(self):
		return '<Deck cards:' + str(self.cards) + '>'

	def add(self, card):
		self.cards.insert(0, card)
	def draw(self):
		return self.cards.pop(0)
	def add_to_bottom(self, card):
		self.cards.append(card)
	def draw_from_bottom(self, card):
		return self.cards.pop(-1)
	def shuffle(self):
		shuffle(self.cards)
	def sort(self, high_first=False, aces_high=False, suits=False):
		if suits:
			card_sort = lambda card: int(card.suit)
		elif high_first and aces_high:
			card_sort = lambda card: -((int(card) - 2) % 14)
		elif high_first:
			card_sort = lambda card: -int(card)
		elif aces_high:
			card_sort = lambda card: (int(card) - 2) % 14
		else:
			basic_sort = lambda card: int(card)

		self.cards = sorted(self.cards, key=card_sort)

	def __getitem__(self, item):
		return self.cards[item]

	def deal(self, piles=None, deck_count=None, card_count=None, even=False):
		cls = type(self)

		if not piles:
			if not deck_count:
				raise ValueError('deal() requires either piles or deck_count as a parameter')

			piles = [cls([]) for i in range(deck_count)]

		if card_count and len(piles) * card_count <= len(self):
			total = len(piles) * card_count
		elif even:
			total = len(self) - (len(self) % len(piles))
		else:
			total = len(self)

		for i in range(total):
			piles[i % len(piles)].add(self.draw())

		return piles

	def _fill_deck(self, jokers=False):
		assert len(self) == 0, 'Can\'t fill a non-empty deck: len=' + str(len(self))

		for suit in range(4):
			for num in range(1, 14):
				self.add_to_bottom(PlayingCard(num, suit))

		if jokers:
			self.add_to_bottom(PlayingCard(0, 0))
			self.add_to_bottom(PlayingCard(0, 1))


class Hand(Pile):

	def hand_sum(cards):
		return sum([int(card) for card in cards])

	def __init__(self, cards=set(), evaluate=hand_sum, name=None, **kwargs):
		self.cards = set(cards)

		self._evaluate = evaluate
		self.properties = kwargs
		if name:
			self['name'] = name

	def __str__(self):
		if 'name' in self.properties:
			cards_str = self['name'] + ': '
		else:
			cards_str = ''

		if len(self) == 0:
			if 'name' in self.properties:
				return cards_str + 'Empty'
			return 'Empty'

		for card in self:
			cards_str += str(card) + ', '
		return cards_str[:-2]
	def __repr__(self):
		return '<Hand name:' + str(self.properties.get('name')) + ', evaluate:' + str(self._evaluate) + \
			', properties:' + str(self.properties) + ', cards:' + str(self.cards) + '>'

	def value(self):
		return self._evaluate(self)
	def view(self):
		visible = self.copy()
		visible.flip_face_up()
		return visible
	def copy(self):
		cls = type(self)
		return cls([card.copy() for card in self], self._evaluate, **self.properties)

	def __getitem__(self, key):
		return self.properties[key]
	def __setitem__(self, key, value):
		self.properties[key] = value
	def __delitem__(self, key):
		del self.properties[key]


class OrderedHand(Hand, Deck):

	def __init__(self, cards=[], evaluate=Hand.hand_sum, name=None, **kwargs):
		self.cards = list(cards)

		self._evaluate = evaluate
		self.properties = kwargs
		if name:
			self['name'] = name

	def __repr__(self):
		return '<Ordered' + Hand.__repr__(self)[1:]


	def __getitem__(self, item):
		if isinstance(item, str):
			return self.properties[item]
		return self.cards[item]
	def __setitem__(self, key, value):
		if not isinstance(key, str):
			raise ValueError('OrderedHand keys can only be strings.')
		self.properties[key] = value
