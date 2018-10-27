# File:    design1.txt
# Author:  Wes Robinson
# Date:    10/22/2018
# Section: 07
# E-mail:  r61@umbc.edu
# Description:  This is the design for the first project
#

##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed #
seed(100)                        #
##################################

#constants for player and monster health
MAX_HEALTH = 100
MIN_HEALTH = 0

DEM_MAX_HEALTH = 300

#constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#constant lists of food and items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]

#List of health effects of each food
FOODS_HEALTH = [-30, -5, 15, 25, 30]

#list of items that can be received
ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys",
         "Walkman", "Laser Cannon", "Rubber Band"]

#Options that you have in the morning
MORNING_OPTIONS = ["View inventory", "View current status",
                   "Eat an Eggo Waffle", "Nothing else"]
#Options that you have when staying or going
DAY_OPTIONS = ["Pack up camp and go", "Stay at camp"]

#Options that you have when fighting the demogorgon
FIGHT_OPTIONS = ["Fight", "Flail", "Flee"]

#Options that you have when eating something from a backpack
PACK_OPTIONS = ["Eat it", "Leave it"]

EQUIP_OPTIONS = ["Equip", "Unequip", "I changed my mind"]

#Game messages
WIN = "CONGRATS! You survived!"
LOSE = "Unfortunately you did not survive..."

#New day message
DAY = "DAY: "

#Stat messages
HP = "Health: "
DIST = "Distance traveled: "
YOURITEM = "Equipped item: "

#Eating message
EAT = "You ate the "
EAT_FAIL = "You already ate one!"
EAT_HEAL = "Your health has increased by: "
EAT_HURT = "Your health has decreased by: "

#Message when demogrogon finds you
SPOTTED = "The Demogorgon has found you. Prepare to yourself..."

#Fleeing messages
FLEE_SUCCESS = "You have fleed successfully!"
FLEE_FAIL = "You have failed to flee!"

#Flail message
FLAIL_MSG = "You have chosen to flail... you succumb to the demogorgon."

#Fighting messages
FIGHT_MSG = "You strike for "
DEM_FIGHT_MSG = "The Demogorgon strikes you for "

#Equipping messages
EQUIP = "You have equipped "
UNEQUIP = "You have unequipped "

#Choice prompt
PROMPT = "Enter a choice: "

#damage values for different items
NONE_DMG = 0
FLASHLIGHT_DMG = 5
WALKTALKIE_DMG = 10
RUBBERBAND_DMG = 25
SWORD_DMG = 50
LASERCANNON_DMG = 100

#numerical effects of different items
BICYCLE_EFFECT = 1.5
HI_C_EFFECT = 0.5
HEELYS_EFFECT = 1.25
WALKMAN_EFFECT = .75

# getUserChoice() asks the user to select a choice from a list of choices
#                 continuously prompts the user until the choice is valid
#                 a valid choice is one that is a valid index in the list
# Input:          choices; a list of all the possible choices available
# Output:         choice; the validated choice that the user made
def getUserChoice(choices):	
	choice = getValidInt(1, len(choices) + 1)
	return choice

# displayMenu()   prints out and of the menus in the program.
#
# Input:          choices; a list of all the possible choices available
# Output:         None
def displayMenu(choices):
	for i in range(len(choices)):
		print(str(i+1) + " - " + choices[i])



# calcDamage()    Computes the amount of damage that the item passed would
#                 inflict when used
# Input:          item; takes in  a string; the item that you want to calculate
#                 damage for
# Output:         damage; the amount of damage that the item inflicts
def calcDamage(item):

    damage = NONE_DMG
    if(item == ITEMS[0] ):
        damage = SWORD_DMG
    elif(item == ITEMS[4]):
        damage = WALKMAN_DMG
    elif(item == ITEMS[5]):
        damage = LASERCANNON_DMG
    elif(item == ITEMS[6]):
        damage = RUBBERBAND_DMG
    elif(item == "Flashlight"):
        damage = FLASHLIGHT_DMG

    return damage

# eat()           Compute the health boost offered by a food that a player has
#                 chosen to eath based on the health value of that food and
#                 player health. (Player health cannot exceed 100).
# Input:          food; the name of the food the layer is going to eat
#                 player_health; the amount of the health the player has before
#                 eating the food item
# Output:         newHealth; an integer, the new health of player after eating
#                 the item
def eat(food, player_health):

    newHealth = player_health

    if(food == FOODS[0]):
        newHealth = FOODS_HEALTH[0]
    elif(food == FOODS[1]):
        newHealth = FOODS_HEALTH[1]
    elif(food == FOODS[2]):
        newHealth = FOODS_HEALTH[2]
    elif(food == FOODS[3]):
        newHealth = FOODS_HEALTH[3]
    elif(food == FOODS[4]):
        newHealth = FOODS_HEALTH[4]

    return newHealth

# fight()         Allow the player to fight The Demogorgon. Fight until someone
#                 someone dies, or you successfully run away. Certain items in
#                 the playing inventory provide special boosts. The player can
#                 also "Flail".
# Input:          player_health; the starting amount of health
#                 item; the item that the player has equipped
#                 inventory; the list of item the palyer has available
# Output:         remHealth; the remaining health the player has after the
#                 fight is concluded


# getValidInt()   Returns a valid integer based off of a minimum and maximum
#                 value, the vaule is between minimum and maximum
# Input:          min; an int which is the minimum int you can input
#                 max; an int which is the maximum int you can input
# Output:         num; the valid integer
def getValidInt(minNum, maxNum):

	num = int(input(PROMPT))
	while(num < minNum and num > maxNum):
		num = int(input(PROMPT))

	return num


# distTraveled()  Returns a float that you travel in one day, it is based off
#                 a function of health and what items you have
# Input:          player_health; your health at the end of the day
#                 inventory; the items you have that my influence distance
# Output:         distance; the amount you traveled in one day
def distTraveled(player_health, inventory):
	distance = 0
	modifier = 1
	if(ITEMS[3] in inventory):
		modifier = HEELYS_EFFECT
	if(ITEMS[1] in inventory):
		modifier = BICYCLE_EFFECT

	distance = ((player_health / 4) + 5) * modifier

	return distance

### put the rest of your function headers here ###

def main():

	curDay = 1
	curDistance = 0.0

	playerHealth = 50

	inventory = ["Walkie Talkie", "Flashlight"]
	equipped = ""

    # while the player isn't dead and hasn't made it far enough
	while(curDistance < SURVIVE_DIST and curDay <= SURVIVE_DAYS):

		
		isMorning = True
		ateWaffle = False
		# perform the daily tasks
		choice = 0
		# while it is still morning

		while(isMorning):
			# show menu with the daily choices you can make
			displayMenu(MORNING_OPTIONS)
			# get a vaild choice <= 4 and >= 1
			choice = getUserChoice(MORNING_OPTIONS)
			print("")
			# if choice is viewing inventory
			if(choice == 1):
				print(inventory)
				print("")
				displayMenu(EQUIP_OPTIONS)
				# get a valid choice <= 3 and >= 1
				choice = getUserChoice(EQUIP_OPTIONS)
				print("")
				# if choice is equipping
				if(choice == 1):
					displayMenu(inventory)
					print("")
					choice = getUserChoice(inventory)
					# equipped item is now choice
					equipped = inventory[choice - 1]
					print(EQUIP + equipped)
					print("")
				# else if choice is unequip
				elif(choice == 2):
					# equipped item is now nothing
					print(UNEQUIP + equipped)
					equipped = ""
				# else do nothing
				else:
					print("")
			# else if choice is viewing your current status
			if(choice == 2):
				# print out health, distance traveled, and equipped item
				print(HP + str(playerHealth))
				print(DIST + str(curDistance))
				print(YOURITEM + equipped)
				print("")
			# else if choice is eating an Eggo Waffle
			elif(choice == 3):
				# add 10 HP to player
				if(not ateWaffle):
					playerHealth += 10
					if(playerHealth >= MAX_HEALTH):
						playerHealth = 100
					# print out that you ate an Eggo Waffle
					print("You ate an Eggo Waffle and gained 10 HP!")
					print("")
				else:
					print(EAT_FAIL)
			# else it is not morning
			else:
				isMorning = False

		# Ask if you stay or go
		choice = getUserChoice(DAY_OPTIONS)

		# if packing up camp
		if(choice == 1)
			# print leaving message
			print("You have decided to leave camp...")
			print("")

			# initiate random event
			randNum = randint(1,10)
			# if backpack at 20% chance
			if(randNum == 1 or randNum == 2):
				# print backpack message
				print("You stumble upon someone's backpack that has been left behind.")
				# initiate random food
				randNum = randint(1,5)
				print("You find: " FOODS[randNum-1])
				print("")
				# get a valid choice to eat or not 2 or 1
				displayMenu(PACK_OPTIONS)
				choice = getUserChoice(PACK_OPTIONS)
				print("")
				# if choice is to eat
				if(choice = 1):
					playerHealth = eat(FOOD[randNum-1], playerHealth)
					print(EAT + FOOD[randNum-1])
					if(FOODS_HEALTH[randNum-1] < 0):
						print(EAT_HURT + str(FOODS_HEALTH[randNum-1]*-1))
					else:
						print(EAT_HEAL + str(FOODS_HEALTH[randNum-1]))
					print("")
				# else go back
				else:
					print("")
            # else if old shed at 20% chance
                # print old shed message
                #print("You stumble upon an old shed lined with shelves.")
                #print("You find: ")
                #initiate random item
                #randint(1,7)
                #Add item ITEM[randomInt] to inventory if not already the inventory
            # else if trench at 20% chance
                # print trench message
                #print("You stumble into a trench. You have to recover for another day")
                # subtract half distance so when adding distTraveled later
                # it totals to positive half distTraveled
                # add extra day
            # else if demogorgon fight at 30% chance
                #fight(playerHealth, equippedItem, inventory)
            # else do nothing

            # set total distance to covered + todays distance traveled
            
            #totalDist += distTraveled(playerHealth, inventory)

        # else if staying
            # print statying message
            #print("You decide to stay and rest at camp")
            # initiate random event
            #randint(1,10)
            # if demogorgon shows up <=7
            #fight(playerHealth, equippedItem, inventory)
            # else HP is set to max

        # increment day
		curDay += 1
        # check to see if we have reached SURVIVE_DAYS or SURVIVE_DIST
            # if win
                # print winning messages and stats
            # else if lose
                # print lossing messages and stats





main()

