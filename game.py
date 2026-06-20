from classes import *
from functions import *

print("\nWelcome to the Flower Fields!")
name = input("What's your name? ")

player = Player(name, 20, generateWeapons())

print("\nHiya " + player.name + ", I need your help!")
print("\nThere's an infestation plaguing my fields and I need you to get to rid of them.\nThere are 6 fields in total. Clearing each field will give you a flower from that field.\nAfter clearing all 6 fields you get to go home with a bouquet of flowers.")

print("\nI already prepared your equipment so you should be good to go!")
print("\nYou have an HP of " + str(player.hp) + " and your starting weapon is " + player.get_item_name() + "." )
print("Your weapon's HP is " + str(player.get_item_hp()) + " and AP is " + str(player.get_item_atk()) + ".")

rooms = generateRooms()
print("\nYou look out to the flower fields and you see the ", end="")
for i, room in enumerate(rooms):
    if i == len(rooms)-1:
        print("and " + room.get_name() + ".", end="")
    else:
        print(room.get_name() + ", ", end="")
room = input("\nWhat field do you want to go into? ")

currentRoom = next((curRoom for curRoom in rooms if curRoom.get_name() == room))
rooms.pop(rooms.index(currentRoom))

print("\nYou enter the " + currentRoom.get_name() + ".")
print("Suddenly you encounter ", end="")
currentEnemies = currentRoom.get_enemies()
for i, enemy in enumerate(currentEnemies):
    if i == len(currentEnemies)-1:
        print("and " + enemy.get_name() + ".", end="")
    else:
        print(enemy.get_name() + ", ", end="")

playerChoice = input("\nWhat will you do? ")