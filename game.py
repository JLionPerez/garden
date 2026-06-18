import random

class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_atk(self):
        return self.atk
    
    def set_hp(self, dmg):
        newHP = self.hp - dmg
        self.hp = newHP
    
    def get_class_name(self):
        return self.__class__.__name__

class Weapon:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp

    def set_hp(self, dmg):
        newHP = self.hp - dmg
        self.hp = newHP
    
    def get_atk(self):
        return self.atk
    
    def get_class_name(self):
        return self.__class__.__name__

class Player:
    def __init__(self, name, hp, item):
        self.name = name
        self.hp = hp 
        self.item = item #barehand is 3 atk

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def set_hp(self, dmg):
        newHP = self.hp - dmg
        self.hp = newHP

    def set_item(self, item):
        self.item = item
    
    def get_item_name(self):
        return self.item.get_name()
    
    def get_item_hp(self):
        return self.item.get_hp()
    
    def set_item_hp(self, dmg):
        self.item.set_hp(dmg)
    
    def get_item_atk(self):
        return self.item.get_atk()

class Room:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

    def get_name(self):
        return self.name

    def get_enemies(self):
        return self.enemies
    
    def get_enemy_name(self, i):
        return self.enemies[i].get_name()

def generateWeapons():
    ladybug = Weapon("Ladybug", 8, 4)
    flySwatter = Weapon("Fly Swatter", 12, 6)
    weedWhacker = Weapon("Weed Whacker", 16, 8)
    bugSpray = Weapon("Bug Spray", 20, 10)

    weaponCache = [ladybug, flySwatter, weedWhacker, bugSpray]
    item = random.choice(weaponCache)
    
    return item

def generateEnemies():
    aphidVals = random.randrange(1, 4)
    spiderMiteVals = random.randrange(1, 4)
    stinkBugVals = random.randrange(1, 6)
    slugVals = random.randrange(1, 6)
    gardenSnailVals = random.randrange(2, 8)
    earwormVals = random.randrange(3, 10)
    mouseSpiderVals = random.randrange(4, 12)

    aphid = Enemy("Aphid", aphidVals, aphidVals)
    spiderMite = Enemy("Spider Mite", spiderMiteVals, spiderMiteVals)
    stinkBug = Enemy("Stink Bug", stinkBugVals, stinkBugVals)
    slug = Enemy("Slug", slugVals, slugVals)
    mouseSpider = Enemy("Mouse Spider", mouseSpiderVals, mouseSpiderVals)
    gardenSnail = Enemy("Garden Snail", gardenSnailVals, gardenSnailVals)
    earworm = Enemy("Earworm", earwormVals, earwormVals)

    item = generateWeapons()

    randomList = [aphid, spiderMite, stinkBug, slug, mouseSpider, gardenSnail, earworm, item]
    random.shuffle(randomList)

    roomList = randomList[:4]

    return roomList

def generateRooms():
    pass

# goal: survive and make a bouquet of flowers from the fields you go through
# asks for player's name will be referred to that name in the game
print("\nWelcome to the Flower Fields!")
name = input("Please enter your name: ")

player = Player(name, 20, generateWeapons())

print("\nHello " + player.name + "!\nYou have an HP of " + str(player.hp) + " and your starting weapon is " + player.get_item_name() + "." )
print("Weapon stats of " + player.get_item_name() + ": ")
print("HP: " + str(player.get_item_hp()) + "    Damage: " + str(player.get_item_atk()))

# testing new item pick up
# player.set_item_hp(2)
# print(player.get_item_hp())

# item = generateWeapons()
# player.set_item(item)
# print(player.get_item_name())
# print(player.get_item_hp())

# testing if enemies are present in room
# firstRoom = Room("Lavender Field", generateEnemies())
# print("\n" + firstRoom.get_name() + " has enemies of: ")
# for e in firstRoom.enemies:
#     print( e.get_class_name() + ": " + e.get_name() + "    HP: " + str(e.get_hp()))
    # print("HP: " + str(e.get_hp()))

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

# clearing out a room gives a flower of from that field to the player