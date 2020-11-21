import cards as c
import os

def clear():
	os.system('clear')

def wait():
	input('\nPress enter to continue...')
	clear()

def hand_value(cards):
	value = 0
	aces = []
	for card in cards:
		if int(card) == 1:
			aces.append(card)
		else:
			value += min(int(card), 10)

	for i, ace in enumerate(aces):
		if value <= 21 - (len(aces) - i - 1) - 11:
			value += 11
		else:
			value += 1

	return value



# Game setup

deck = c.Deck(fill=True)
deck.shuffle()

print('Welcome to Big Blackjack!')
print('We hope you enjoy your time.\n')

player_count = 0
while player_count == 0:
	try:
		player_count = int(input('How many players will be joining us: '))
		if player_count < 1:
			print('At least one player is required.')
			player_count = 0
	except ValueError:
		print('Enter a number please.')

players = []
for i in range(player_count):
	name = input('Enter player ' + str(i+1) + '\'s name: ')
	players.append(c.OrderedHand(evaluate=hand_value, name=name, money=100))

dealer = c.OrderedHand(name='The Dealer', evaluate=hand_value, hold=False)

clear()
print('The dealer has arrived!')
print('They look awfully confident.')
print('Think you can outwit them?\n')
input('Press enter to begin...')
clear()



# Game loop

while len(players) > 0:
	everyone = players + [dealer]

	for player in players:
		print(str(player['name']) + ' has $' + str(player['money']))

	wait()

	# Betting loop
	for player in players:
		bet = 0
		while bet == 0:
			try:
				bet = int(input('How much will ' + player['name'] + ' bet: '))
				if bet > player['money']:
					print('You must have enough money to cover the bet.')
					bet = 0
				elif bet < 1:
					print('The bet must be at least $1.')
					bet = 0
			except ValueError:
				print('Enter a number please.')
		player['bet'] = bet
		player['value'] = 0
		player['hold'] = False

	wait()

	deck.deal(piles=everyone, card_count=2)
	for player in everyone:
		player[-1].flip()

	# Hand loop
	while not all([player['hold'] for player in everyone]):

		# Player loop
		for player in [player for player in players if not player['hold']]:
			print('It is', player['name'] + '\'s turn!')
			wait()

			for p in everyone:
				print(str(p) + (' - HOLD' if p['hold'] else ''))

			print()
			print(player.view())
			print()

			value = player.value()
			if value > 21:
				print('You\'ve busted! Bummer.')
				player['hold'] = True
				player['value'] = 0
			elif value == 21:
				print('You\'ve hit 21! Nice!')
				player['hold'] = True
				player['value'] = 21
			else:
				player['value'] = value

			if not player['hold']:
				player['hold'] = None
				while player['hold'] == None:
					choice = input('HIT or HOLD: ')
					if choice.upper() == 'HIT':
						player['hold'] = False
					elif choice.upper() == 'HOLD':
						player['hold'] = True
					else:
						print('Enter HIT or HOLD please.')
			print()

			if not player['hold']:
				player.add(deck.draw())
				print(player.view())
				value = player.value()
				if value > 21:
					print('You\'ve busted! Bummer.')
					player['hold'] = True
					player['value'] = 0
				elif value == 21:
					print('You\'ve hit 21! Nice!')
					player['hold'] = True
					player['value'] = 21
				else:
					player['value'] = value

			wait()

		# Dealer's turn
		if not dealer['hold']:
			print('It\'s the dealer\'s turn!')
			wait()

			print('The dealer is playing...\n')

			for player in everyone:
				print(str(player) + (' - HOLD' if player['hold'] else ''))
			print()

			value = dealer.value()
			if value > 21:
				dealer['value'] = 0
				dealer['hold'] = True
			elif value == 21:
				dealer['value'] = 21
				dealer['hold'] = True
			else:
				dealer['value'] = value

			if not dealer['hold']:
				dealer['hold'] = value > 16

			if dealer['hold']:
				print('The dealer HOLDs.')
			else:
				print('The dealer HITs.')
			print()

			if not dealer['hold']:
				dealer.add(deck.draw())
				print(dealer)
				value = dealer.value()
				if value > 21:
					dealer['value'] = 0
					dealer['hold'] = True
				elif value == 21:
					dealer['value'] = 21
					dealer['hold'] = True
				else:
					dealer['value'] = value

			wait()

	# Hand wrap-up

	print('Everyone has held')
	wait()
	dealer['hold'] = False

	for player in everyone:
		player.flip_face_up()
		print(player)
		deck += player
	deck.shuffle()

	print()
	losers = []
	for player in players:
		if player['value'] >= dealer['value']:
			print(str(player['name']) + ' won $' + str(player['bet']) + '!')
			player['money'] += player['bet']

		else:
			print(str(player['name']) + ' lost $' + str(player['bet']) + '.')
			player['money'] -= player['bet']

			if player['money'] < 1:
				print(str(player['name']) + ' has lost! Oh no!')
				losers.append(player)


	for loser in losers:
		players.remove(loser)

	wait()

print('We hope you have enjoyed Big Blackjack!')
print('Come again soon <3')
print()