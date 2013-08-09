Notes On Design
===============


Room types
----------
The room types should not be symmetric. In other words, Residential rooms should not serve the same purpose in your tower as Office rooms. Think the resources in Power Grid and how their purposes morph over time, as opposed to the colors of track in Ticket to Ride. 

This is being accomplished in a few ways:
* Residential Clients require fewer rooms in general. They are more flexible in this way and can fit anywhere, but there are fewer Residential Room tiles and they won't award as many $. To make up for this disadvantage, their abilities should be more powerful and more interestingly interactive than the other types.
* Retail Clients require wider areas (horizontally) to fit than Office tiles, though the number of rooms required is similar. Assuming a tendency for towers to narrow near the top, this means Retail Clients will be lower in your building and likely bought up and cashed in earlier in the game.
* Office Clients are in contrast to Retail in that they require taller areas. This means they can fit into the top of your tower, and are likely to be cashed in later on. 

Hopefully this assymmetry leads to some competition between players in Client selection, since there are better and worse cards depending on the stage of the game. 


Quick Numbers
-------------
5 rounds * 15 tiles/rnd = 75 total tiles per player, on average (excluding abilities)

Average #rooms per pattern = 4, 5 rounds * 2 client/rnd = 40 filled rooms, excluding the option of filling a pattern multiple times. Wild estimate of 1/3 clients get 2 patterns filled, 1/10 get 3 patterns filled = 56 rooms filled = $56. 

Height at 6-wide = 13, 5-wide = 15, 4-wide = 19. Average probably 16.
With height bonuses, 56 rooms filled now = $56 + $24 + $4 = $84


Test Number
-----------
8 rounds, 10 tiles/rnd = 80 tiles.

Game 1, Strategy: Retail on the bottom, tower of offices up.
Total $ = 43. Double-score tiles: 5

Game 2, Strategy: 6-wide straight up.
28 + 22(11x2) + 6(2x3) = $56

Game 3, Strategy: slanted in, get higher before cashing a lot
$60.

Changes
=======
Problem: There are too many abilities.
I think I'll make only half the cards have abilities, and those with abilities will be harder to actually place. 

Problem: I think there's a big advantage to just growing the bottom of your tower out horizontally for retail purposes?
One solution to this solves a few other potential problems. Make a small max hand size, like 3, so that you can't store up retail cards. This means you're more often playing with what you've got in the moment, and planning for the future is about heuristics of building instead of hoarding cards. 

Problem: Elevators are weird and don't matter very much.
Elevators are now replaced by stairs-with-stacking-bonus. Rooms on a floor can't be cashed in unless there are stairs from the ground to that floor. You get a bonus for a stair tile directly above another stair tile (now it's an elevator.)

Problem: Time component doesn't make a lot of sense, I suspect. Maybe it works if you have to flip over your Tiles to see what they are, but if not then you can use the "look at client cards" time to plan your moves.
Remove the time component for now. Replace "fastest builder gets first pick" with "tallest tower gets first pick."

Problem: Office and Retail types are not differentiated enough. 
I need to be more serious about designing retail horizontally, and office vertically. I also need to make retail cards have abilities which matter more early in the game, and office matter more late in the game. Residential can go either way. 

Problem: Potentially screwed by elevator tile randomness

Elevator/Stairs
---------------
Good things:
* Provide an extra piece type to break up the room types and make pattern creation more difficult.
* Provide a way to limit height growth sanely
* Are an obvious feature of real-life skyscrapers, including them makes more natural-looking skyscrapers

Bad things:
* Too random! It can screw you temporarily and totally screw you if you get very unlucky.
* There's not a lot of choice about it (although a bit better now that the stairs system exists) 

Vague solutions:
* A way of assuring you can always have enough elevator tiles
* A way of trading in tiles in general

Solution for now:
* Trade any two tiles in for a specific tile of your choice. 