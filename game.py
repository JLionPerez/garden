import random

class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

class Player:
    def __init__(self, name, hp, item):
        self.name = name
        self.hp = hp 
        self.item = item #changes depending on what type of weapon they have if they don't have one it's 3 dmg (barehanded)

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_item_name(self):
        return self.item.get_name()
    
    def get_item_hp(self):
        return self.item.get_hp()
    
    def get_item_dmg(self):
        return self.item.get_dmg()
    


class Weapon:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp

    def set_hp(self, dmg):
        return self.hp - dmg
    
    def get_dmg(self):
        return self.dmg

class Room:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

# goal: survive and make a bouquet of flowers from the fields you go through

# player has 20 hp
# asks for player's name will be referred to that name in the game
# randomized weapon at start, can only equip one weapon at a time
# weapons:
    # weed whacker, dmg: 8
    # fly swatter, dmg: 6
    # bug spray, dmg: 10
    # ladybugs, dmg: 4

ladybug = Weapon("Ladybug", 8, 4)
flySwatter = Weapon("Fly Swatter", 12, 6)
weedWhacker = Weapon("Weed Whacker", 16, 8)
bugSpray = Weapon("Bug Spray", 20, 10)

weaponCache = []
weaponCache.append(ladybug)
weaponCache.append(flySwatter)
weaponCache.append(weedWhacker)
weaponCache.append(bugSpray)

print("\nWelcome to the Flower Fields!")
name = input("Please enter your name: ")

item = random.choice(weaponCache)

player = Player(name, 20, item)

print("\nHello " + player.name + "!\nYou have an HP of " + str(player.hp) + " and your starting weapon is " + player.get_item_name() + "." )
print("Weapon stats of " + player.get_item_name() + ": ")
print("HP: " + str(player.get_item_hp()) + "    Damage: " + str(player.get_item_dmg()))

# 6 rooms generated: lavender field, marigold field, sunflower field, rose field, dahlia field, daisies field
    # each room have 4 entities
        # 4 enemies OR 3 enemies and 1 item
        # to do this we have a list say 5
        # 4 enemies and 1 weapon 
        # randomly select a weapon add that to the list of 5
        # randomly select enemies and add that to the list of 5 too
        # they will be added into the list randomly so use random.shuffle()
        # first 4 from the list will be the entities in the room, thats how we do the may or may not have weapon in room part


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