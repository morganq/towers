from PIL import Image, ImageFont, ImageDraw
import textwrap
import re

title_font = ImageFont.truetype("verdanab.ttf", 50)
title_font_sm = ImageFont.truetype("verdanab.ttf", 30)
ability_font = ImageFont.truetype("verdana.ttf", 30)
flavor_font = ImageFont.truetype("verdanai.ttf", 25)


title_rect = (40, 26, 430, 48)
title_rect_sm = (40, 38, 430, 48)
ability_rect = (40, 700, 600, 300)
flavor_rect = (40, 720, 600, 100)

card_base = Image.open("card_base.png")

pattern_base = Image.open("pattern_base.png")

default_graphic = Image.open("default_image.png")

card_title_bars = {
	"Retail":Image.open("bar_retail.png"),
	"Office":Image.open("bar_office.png"),
	"Resident":Image.open("bar_resident.png")
}

card_pattern_bits = {
	"Retail":Image.open("pattern_bit_retail.png"),
	"Office":Image.open("pattern_bit_office.png"),
	"Resident":Image.open("pattern_bit_resident.png"),
}

f = open("../../cards.md")
raw = f.read()
raw = raw.replace("\r","")
regex1 = re.compile("(.+?)\n--(-+)\n(.+?)\n\n\n", re.DOTALL)
regex2 = re.compile("(.+?)\n([x\W]+)\n*?([^\"]+)?\n*?(\".+\")?.*", re.DOTALL)
all_cards = regex1.findall(raw)

def multitext(draw, rect, text, font, width=41, dy=35):
	lines = textwrap.wrap(text, width=width)
	y = rect[1]
	for line in lines:
		tr = (rect[0], y, rect[2], rect[3])
		draw.text(tr, line, font=font, fill=(0,0,0))
		y += dy
	return y

def patternImg(pattern, tileType):
	bit = card_pattern_bits[tileType]
	trows = filter(lambda x:'x' in x, pattern.split("\n"))
	
	h = len(trows)
	if h == 0: return None
	w = max([len(r.rstrip()) for r in trows])
	im = Image.new('RGBA', (w * 110, h * 110), (255,255,255,0))
	x = 0
	y = 0
	for r in trows:
		for c in r:
			if c == 'x':
				im.paste(bit, (x,y), bit)
			x += 110
		y += 110
		x = 0
	return im

i = 0
for card in all_cards:
	name = card[0]
	filename = name.replace(" ", "_").replace("'", "").replace('"', "").replace("*","")
	info = card[2]
	grps = regex2.match(info).groups()
	cardType = grps[0]
	pattern = grps[1]
	ability = grps[2]
	flavor = grps[3]
	im = card_base.copy()
	draw = ImageDraw.Draw(im)
	im.paste(card_title_bars[cardType], (0,0), card_title_bars[cardType])
	im.paste(default_graphic, (20, 100))
	im.paste(pattern_base, (0, 0), pattern_base)

	if len(name) < 18:
		draw.text(title_rect, name, font=title_font, fill=(0,0,0))
	else:
		draw.text(title_rect_sm, name, font=title_font_sm, fill=(0,0,0))

	ay = flavor_rect[1]
	if ability:
		ay = multitext(draw, ability_rect, ability, ability_font)

	fr = [flavor_rect[0], ay + 20, flavor_rect[2], flavor_rect[3]] 
	if flavor:
		multitext(draw, fr, flavor, flavor_font)

	pat = patternImg(pattern, cardType)
	if pat:
		pat.thumbnail((150,150))
		px = 646
		py = 188
		im.paste(pat, (px-pat.size[0]/2,py-pat.size[1]/2), pat)

	im.save("img/"+filename+".png")
	print i
	i+=1



