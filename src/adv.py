from room import Room
from player import Player
from item import Item

# possible commands
commands = {'n': 'move north', 's': 'move south', 'e': 'move east', 'w': 'move west', 'i': 'player inventory', 'ak': 'action key', 'q': 'quit game'}

# declare all the rooms
room = {
	'outside': Room(
		'Outside Cave Entrance',
		'''North of you, the cave mount beckons'''
	),
	'foyer': Room(
		'Foyer',
		'''Dim light filters in from the south. Dusty passages run north and east.'''
	),
	'overlook': Room(
		'Grand Overlook',
		'''A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.'''
	),
	'narrow': Room(
		'Narrow Passage',
		'''The narrow passage bends here from west to north. The smell of gold permeates the air.'''
	),
	'treasure': Room(
		'Treasure Chamber',
		'''You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.'''
	)
}

# declare items
items = {
	'cloak-of-agility': Item(
		'cloak-of-agility',
		'''increase speed and dexterity'''
	),
	'broken-angel-wings': Item(
		'broken-angel-wings',
		'''wings of an angel which give the ability to fly, but they need to be mended...'''
	),
	'pickaxe': Item(
		'pickaxe',
		'''strong pickaxe used for mining, but where...'''
	),
	'chest-1': Item(
		'chest-1',
		'''a trap! this chest is a mimic, picking it up causes immediate death'''
	),
	'chest-2': Item(
		'chest-2',
		'''a trap! this chest is a mimic, picking it up causes immediate death'''
	),
	'chest-3': Item(
		'chest-3',
		'''you found a chest, but it is locked...'''
	)
}

# link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to rooms
room['foyer'].roomItems.append(items['cloak-of-agility'])
room['overlook'].roomItems.append(items['broken-angel-wings'])
room['narrow'].roomItems.append(items['pickaxe'])
room['treasure'].roomItems.extend([items[chest] for chest in items if 'chest' in chest])

def printActions():
	print('\naction key')
	for commandKey in commands:
		print(f'{commandKey} - {commands[commandKey]}')
	print()

def printInventory(inventory):
	print('\nplayer inventory')
	for item in inventory:
		print(item)
	print()

def commandParser(command, activePlayer):
	if len(command.split()) >= 2:
		commandList = command.split()
		if (commandList[0] == 'get') or commandList[0] == 'take':
			for item in activePlayer.currentRoom.roomItems:
				if commandList[1].lower() in item.name.lower():
					if item.name.lower() == commandList[1].lower():
						activePlayer.playerItems.append(item)
						activePlayer.currentRoom.roomItems.remove(item)
						item.onTake()
						return
					else:
						print('\nto get an item make sure you type it the same way that it is shown in room items\n')
				else:
					print(f'\n{commandList[1]} not found in current room\n')
					return
		elif commandList[0] == 'drop':
			for item in activePlayer.playerItems:
				if commandList[1].lower() in item.name.lower():
					if item.name.lower() == commandList[1].lower():
						activePlayer.playerItems.remove(item)
						activePlayer.currentRoom.roomItems.append(item)
						item.onDrop()
						return
					else:
						print('\nto drop an item make sure you type it the same way that it is shown in player inventory\n')
				else:
					print(f'\n{commandList[1]} not found in player items\n')
					return
	elif len(command.split()) == 1:
		if command == 'n':
			if activePlayer.currentRoom.n_to != None:
				print('\nmoving north...\n')
				activePlayer.currentRoom = activePlayer.currentRoom.n_to
			else:
				print('\nthere is no room north of the current room\n')
		elif command == 's':
			if activePlayer.currentRoom.s_to != None:
				print('\nmoving south...\n')
				activePlayer.currentRoom = activePlayer.currentRoom.s_to
			else:
				print('\nthere is no room south of the current room\n')
		elif command == 'e':
			if activePlayer.currentRoom.e_to != None:
				print('\nmoving east...\n')
				activePlayer.currentRoom = activePlayer.currentRoom.e_to
			else:
				print('\nthere is no room east of the current room\n')
		elif command == 'w':
			if activePlayer.currentRoom.w_to != None:
				print('\nmoving west...\n')
				activePlayer.currentRoom = activePlayer.currentRoom.w_to
			else:
				print('\nthere is no room west of the current room\n')
		elif (command == 'i') or (command == 'inventory'):
			printInventory(activePlayer.playerItems)
		elif command == 'ak':
			printActions()
		else:
			print('\ninvalid command - to see the action key input the command [ak]\n')
	# else:
	# 	for item in items:
	# 		if command.split()[1] in items[item].name:
	# 			print('\nto get an item make sure you type it the same way that it is shown\n')
		# print('\ninvalid command - to see the action key input the command [ak]\n')

def main():
	print('Adventure Game')
	printActions()
	activePlayer = Player(input('enter your player name - '), room['outside'])
	print()

	while True:
		print(activePlayer.currentRoom)

		playerCommand = input('enter command for next action - ')

		if playerCommand == 'q':
			break
		commandParser(playerCommand, activePlayer)

main()
