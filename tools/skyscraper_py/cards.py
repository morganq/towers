import sys
from random import shuffle, randint

class Card:
	def __init__(self, name, description):
		self.name = name
		self.description = description


deck = []
def addToDeck(c, count):
	for i in range(count):
		deck.append(c)


addToDeck(Card("DrugCorp (z)", "Retail"), 4)
addToDeck(Card("Variety Freshly Canned Foods (r)", "Retail"), 2)
addToDeck(Card("Top Service Deli (4h)", "Retail"), 3)
addToDeck(Card("Pinnacle Suits & Attire (T')", "Retail"), 2)
addToDeck(Card("Mom & Pop Federation (2h)", "Retail"), 3)
addToDeck(Card("FutureTek Showroom (T inverted)", "Retail"), 3)
addToDeck(Card("SkyLite Souvenirs (3h)", "Retail"), 2)
addToDeck(Card("World Famous Revolving Espresso Bar (4h)", "Retail"), 2)
addToDeck(Card("Fat Tony's Legitimate Meat Shop (x6)", "Retail"), 3)
addToDeck(Card("Coffee Shop Megacorp (: :)", "Retail"), 5)
addToDeck(Card("Generic Retail A (3h)", "Retail"), 10)
addToDeck(Card("Generic Retail B (4h)", "Retail"), 20)

addToDeck(Card("Edge Financial (2x3)", "Office"), 3)
addToDeck(Card("High Tower Builder's Union (5v)", "Office"), 3)
addToDeck(Card("RightMessage Marketing Professionals (+)", "Office"), 3)
addToDeck(Card("Payne & Son Security (r + 2 on top)", "Office"), 3)
addToDeck(Card("No Such Agency (r + 2 below)", "Office"), 2)
addToDeck(Card("QBQ Technologies Satellite Office (block)", "Office"), 3)
addToDeck(Card("Acme Capital Appropriations (b)", "Office"), 3)
addToDeck(Card("Non-Generic Office (4v)", "Office"), 10)
addToDeck(Card("Generic Office A (3v)", "Office"), 10)
addToDeck(Card("Generic Office B (4v)", "Office"), 20)

addToDeck(Card("Chip \"Fr0stBrn\" Winkleton, Hacker (.)", "Residential"), 3)
addToDeck(Card("Sir blah, Advisor to the Queen (2h)", "Residential"), 3)
addToDeck(Card("Genevieve Moonspirit, Psychic (2v)", "Residential"), 3)
addToDeck(Card("Simone Cattleberry, Hipster (2h)", "Residential"), 3)
addToDeck(Card("Non-Generic Residential (2v)", "Residential"), 3)
addToDeck(Card("Generic Residential (.)", "Residential"), 15)


shuffle(deck)

def showCards(lod):
	for i in range(len(lod)):
		print str(i) + ": " + lod[i].name + ": " + lod[i].description

revealed = []
mine = []
order = 0
roundNum = 0

while 1:
	cmd = raw_input(">").strip()
	if cmd == "round":
		print "round " + str(roundNum)
		revealed = deck[:6]
		deck = deck[6:]
		showCards(revealed)
		roundNum += 1


	if cmd == "pick1":
		order = randint(0,2)
		print "order: " + str(order)
		for i in range(order):
			del revealed[randint(0, len(revealed)-1)]
		showCards(revealed)

	if cmd == "pick2":
		for i in range(4-order*2):
			del revealed[randint(0, len(revealed)-1)]
		showCards(revealed)

	if cmd >= "0" and cmd <= "6":
		mine.append(revealed[int(cmd)])
		del revealed[int(cmd)]

	if cmd == "mine":
		showCards(mine)

	if cmd[:4] == ("use "):
		if cmd[4:] >= "0" and cmd[4:] <= "9":
			del mine[int(cmd[4:])]

	elif cmd == "quit":
		break