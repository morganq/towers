import sys
from random import shuffle

class Card:
	def __init__(self, name, description):
		self.name = name
		self.description = description


deck = []
def addToDeck(c, count):
	for i in range(count):
		deck.append(c)


addToDeck(Card("", "$4 res-hotel"), 3)
addToDeck(Card("", "$2 res"), 5)
addToDeck(Card("", "$3 office-tech"), 3)
addToDeck(Card("", "$3 office-finance"), 3)
addToDeck(Card("", "$5 office-finance"), 1)
addToDeck(Card("", "$3 office-media"), 4)
addToDeck(Card("", "$7 retail"), 3)
addToDeck(Card("", "$8 single office"), 3)
addToDeck(Card("", "Swap clients (random)"), 3)
addToDeck(Card("", "Swap clients (their choice)"), 3)
addToDeck(Card("", "Swap clients"), 3)

shuffle(deck)

revealed = []

while 1:
	cmd = raw_input(">").strip()
	if cmd == "round":
		revealed = deck[:5]
		deck = deck[5:]
		for i in range(len(revealed)):
			print str(i) + ": " + revealed[i].name + ": " + revealed[i].description

	elif cmd == "quit":
		break