import random
from classes import *

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