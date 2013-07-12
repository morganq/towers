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

residential = TileType("Res...", (128,255,128), "horizontal")
elevator = TileType("Ele...", (128,128,128), "vertical")
office = TileType("Office", (255,128,128), "any")
retail = TileType("Retail", (128,128,255), "bottom")

class Tile:
	def __init__(self, tileType, tileSubtype = None, tileFeature = None):
		self.tileType = tileType
		self.tileSubtype = tileSubtype
		self.tileFeature = tileFeature

t_res_hot_base = Tile(residential, "Hotel")
t_res_con_base = Tile(residential, "Condo")
t_res_pen_base = Tile(residential, "Penthouse")

t_off_fin_base = Tile(office, "Financial")
t_off_tec_base = Tile(office, "Technology")
t_off_med_base = Tile(office, "Media")

t_elevator = Tile(elevator)

t_retail_base = Tile(retail)

tileDeck = []
clientDeck = []

def addTiles(tileType, num=1):
	for i in range(num):
		tileDeck.append(tileType)

def addClients(clientType, num=1):
	for i in range(num):
		clientDeck.append(clientType)

addTiles(t_res_hot_base, 10)
addTiles(t_res_con_base, 10)
addTiles(t_res_pen_base, 10)
addTiles(t_off_fin_base, 10)
addTiles(t_off_tec_base, 10)
addTiles(t_off_med_base, 10)
addTiles(t_elevator, 20)
addTiles(t_retail_base, 10)

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

	if t.tile.tileSubtype:
		textSurf = font.render(t.tile.tileSubtype, True, (0,0,0))
		s.blit(textSurf, (w / 2 - textSurf.get_width() / 2 + x, h / 2 + y))

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

tilesPerHand=12

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
			if tileToPlace:
				tileToPlace.position = (event.pos[0] / gridSize, event.pos[1] / gridSize)
				placedTiles.append(tileToPlace)
				tileToPlace = None
			else:
				tileToPlace = grabHandTileAt(event.pos)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				newTileHand()
			if event.key == pygame.K_BACKSPACE:
				tileHand = []
				tileToPlace = None

	drawState(screen)
	if tileToPlace is not None:
		mp = pygame.mouse.get_pos()
		drawTileAt(screen, tileToPlace, mp[0] - gridSize /2, mp[1] - gridSize/2)

	pygame.display.update()