import pygame
import sys
from random import shuffle

pygame.init()
screen = pygame.display.set_mode((48 * 20, 48 * 16))

class TileType:
	def __init__(self, name, color, scoringArrangement):
		self.name = name
		self.color = color
		self.scoringArrangement = scoringArrangement

residential = TileType("Res...", (240,240,24), "horizontal")
elevator = TileType("Ele...", (128,64,148), "vertical")
office = TileType("Office", (64,64,255), "any")
retail = TileType("Retail", (220,64,64), "bottom")

class Tile:
	def __init__(self, tileType):
		self.tileType = tileType

t_retail = Tile(retail)

t_office = Tile(office)

t_elevator = Tile(elevator)

t_residential = Tile(residential)

tileDeck = []
clientDeck = []
scored = []

def addTiles(tileType, num=1):
	for i in range(num):
		tileDeck.append(tileType)

def addClients(clientType, num=1):
	for i in range(num):
		clientDeck.append(clientType)

addTiles(t_retail, 30)
addTiles(t_office, 30)
addTiles(t_elevator, 15)
addTiles(t_residential, 15)

shuffle(tileDeck)
shuffle(clientDeck)

tileHand = []

font = pygame.font.SysFont("Arial", 12)

class PlacedTile:
	def __init__(self, tile, position):
		self.tile = tile
		self.position = position


gridSize = 48

def drawTileAt(s, t, x, y):
	w,h = (gridSize, gridSize)
	pygame.draw.rect(s, t.tile.tileType.color, pygame.Rect(x, y, w, h))

	textSurf = font.render(t.tile.tileType.name, True, (0,0,0))
	s.blit(textSurf, (w / 2 - textSurf.get_width() / 2 + x, h / 2 - 12 + y))

def drawPlacedTile(s, t):
	x = t.position[0] * gridSize
	y = t.position[1] * gridSize
	drawTileAt(s, t, x, y)		

def drawState(s):
	s.fill((255,255,255))
	
	for pt in tileHand:
		drawPlacedTile(s, pt)

	for pt in placedTiles:
		drawPlacedTile(s, pt)

	for pt in scored:
		pygame.draw.circle(s, (0,0,0), pt, gridSize / 4, 0)

	for i in range(screen.get_width() / gridSize):
		pygame.draw.line(s, (0, 0, 0), (i*gridSize, 0), (i*gridSize, screen.get_height()))
	for i in range(screen.get_height() / gridSize):
		pygame.draw.line(s, (0, 0, 0), (0, i*gridSize), (screen.get_width(), i*gridSize))			

def grabHandTileAt(pos):
	if pos[0] > gridSize or pos[1] > gridSize * len(tileHand):
		return None
	i = pos[1] / gridSize
	for j in range(i, len(tileHand)):
		tileHand[j].position = (tileHand[j].position[0], tileHand[j].position[1] - 1)
	return tileHand.pop(i)

tilesPerHand=10

def newTileHand():
	global tileHand
	global tileDeck
	for i in range(len(tileHand), tilesPerHand):
		tileHand.append( PlacedTile(tileDeck[i], (0, i)) )
	tileDeck = tileDeck[tilesPerHand:]

newTileHand()

placedTiles = []

tileToPlace = None

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if tileToPlace:
					tileToPlace.position = (event.pos[0] / gridSize, event.pos[1] / gridSize)
					placedTiles.append(tileToPlace)
					tileToPlace = None
				else:
					tileToPlace = grabHandTileAt(event.pos)
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 3:
				scored.append(event.pos)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				newTileHand()
			if event.key == pygame.K_BACKSPACE:
				tileHand = []
				tileToPlace = None
			if event.key == pygame.K_e:
				tileHand.append(PlacedTile(t_elevator, (0,len(tileHand)) ))

	drawState(screen)
	if tileToPlace is not None:
		mp = pygame.mouse.get_pos()
		drawTileAt(screen, tileToPlace, mp[0] - gridSize /2, mp[1] - gridSize/2)

	pygame.display.update()