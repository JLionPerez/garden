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
    
    def isRoomCleared(self):
        if not self.enemies:
            return False
        return True

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

    enemies = randomList[:4]

    return enemies

def generateRooms():
    lavenderFields = Room("Lavender Fields", generateEnemies())
    marigoldFields = Room("Marigold Fields", generateEnemies())
    sunflowerFields = Room("Sunflower Fields", generateEnemies())
    roseFields = Room("Rose Fields", generateEnemies())
    dahliaFields = Room("Dahlia Fields", generateEnemies())
    poppyFields = Room("Poppy Fields", generateEnemies())

    rooms = [lavenderFields, marigoldFields, sunflowerFields, roseFields, dahliaFields, poppyFields]
    random.shuffle(rooms)

    return rooms

print("\nWelcome to the Flower Fields!")
name = input("What's your name? ")

player = Player(name, 20, generateWeapons())

print("\nHiya " + player.name + ", I need your help!")
print("\nThere's an infestation plaguing my fields and I need you to get to rid of them.\nThere are 6 fields in total. Clearing each field will give you a flower from that field.\nAfter clearing all 6 fields you get to go home with a bouquet of flowers.")

print("\nI've readied your equipment so you should be good to go!")
print("\nYou have an HP of " + str(player.hp) + " and your starting weapon is " + player.get_item_name() + "." )
print("Your weapon's HP is " + str(player.get_item_hp()) + " and AP is " + str(player.get_item_atk()) + ".")
# print("HP: " + str(player.get_item_hp()) + "    Attack Points: " + str(player.get_item_atk()))

# player chooses what field to start with
# clearing out a room gives a flower of from that field to the player
# rooms = generateRooms()
# for room in rooms:
#     print()





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