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