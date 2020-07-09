from room import Room
from player import Player
from item import Item

allCommands = {
	# possible movement commands
	'movementCommands': {
		'n': 'move north',
		's': 'move south',
		'e': 'move east',
		'w': 'move west'
	},
	# possible item commands
	'itemCommands': {
		'i': 'player inventory',
		'get': 'pick up item',
		'take': 'pick up item',
		'drop': 'drop item'
	},
	# core game commands
	'coreCommands': {
		'ak': 'action key',
		'q': 'quit game'
	},
	# possible directions
	'directions': {
		'n': 'north',
		's': 'south',
		'e': 'east',
		'w': 'west'
	}
}

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
	for commandType in allCommands:
		for commandKey in allCommands[commandType]:
			 print(f'{commandKey} - {allCommands[commandType][commandKey]}')
	print()

# def commandParser(command, activePlayer):

def main():
	print('Adventure Game')
	printActions()
	activePlayer = Player(input('enter your player name - '), room['outside'])
	print()

	while True:
		print(activePlayer.currentRoom)

		playerCommandList = input('enter command for next action - ').lower().split()

		if playerCommandList[0] == 'q':
			break
		elif playerCommandList[0] in allCommands['directions']:
			activePlayer.checkMovementCommand(allCommands['directions'][[playerCommandList][0][0]])
		elif playerCommandList[0] in allCommands['itemCommands']:
			activePlayer.handleItemCommand(playerCommandList)
		else:
			print('\ninvalid command - to see the action key input the command [ak]\n')


		# commandParser(playerCommandList, activePlayer)
		# if any(('chest-1' in item.name) or ('chest-2' in item.name) for item in activePlayer.playerItems):
		# 	print('the chest is actually a mimic, as you pick up the chest it emerges and kills you quickly. you died')
		# 	break

main()
