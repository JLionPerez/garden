import random

class Enemy:
    def __init__(self, type, hp, dmg):
        self.type = type
        self.hp = hp
        self.dmg = dmg

class Player:
    def __init__(self, name, hp, item):
        self.name = name
        self.hp = hp 
        self.item = item #changes depending on what type of weapon they have if they don't have one it's 3 dmg (barehanded)

class Weapon:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

ladybugs = Weapon("Ladybugs", 8, 4)
flySwatter = Weapon("Fly Swatter", 12, 6)
weedWhacker = Weapon("Weed Whacker", 16, 8)
bugSpray = Weapon("Bug Spray", 20, 10)

weaponCache = []
weaponCache.append(ladybugs)
weaponCache.append(flySwatter)
weaponCache.append(weedWhacker)
weaponCache.append(bugSpray)

print("Welcome to the Flower Fields!")
name = input("Please enter your name: ")

item = random.choice(weaponCache)

player = Player(name, 20, item)

print("Hello " + player.name + "! You have an HP of " + str(player.hp) + " and your starting weapon is " + player.item.name + "." )

# weaponCache = {
#     "Ladybugs": 4,
#     "Fly Swatter": 6,
#     "Weed Whacker": 8,
#     "Bug Spray": 10
# }

# goal: survive and make a bouquet of flowers from the fields you go through

# player has 20 hp
# asks for player's name will be referred to that name in the game
# randomized weapon at start, can only equip one weapon at a time
# weapons:
    # weed whacker, dmg: 8
    # fly swatter, dmg: 6
    # bug spray, dmg: 10
    # ladybugs, dmg: 4
# 6 rooms generated: lavender field, marigold field, sunflower field, rose field, dahlia field, daisies field
    # each room have 4 entities
        # 4 enemies OR 3 enemies and 1 item
# player chooses what field to start with
# enemies:
    # weak: 
        # aphid, hp and dmg: d4
        # spider mite, hp and dmg: d4
        # stink bug, hp and dmg: d6
        # slug, hp and dmg: d6
    # strong:
        # Mouse Spider, hp and dmg: d12
        # Garden Snail, hp and dmg: d8
        # Earworm, hp and dmg: d10
# clearing out a room gives a flower of from that field to the player

