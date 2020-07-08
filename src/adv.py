from room import Room
from player import Player

commands = {'n': 'move north', 's': 'move south', 'e': 'move east', 'w': 'move west', 'ak': 'action key', 'q': 'quit game'}

# Declare all the rooms

room = {
	'outside': Room(
		"Outside Cave Entrance",
		"North of you, the cave mount beckons"
	),
	'foyer': Room(
		"Foyer",
		"""Dim light filters in from the south. Dusty passages run north and east."""
	),
	'overlook': Room(
		"Grand Overlook",
		"""A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
	),
	'narrow': Room(
		"Narrow Passage",
		"""The narrow passage bends here from west to north. The smell of gold permeates the air."""
	),
	'treasure': Room(
		"Treasure Chamber",
		"""You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""
	)
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

def printActions():
	print('\naction key')
	for commandKey in commands:
		print(f'{commandKey} - {commands[commandKey]}')
	print()

def commandParser(command, activePlayer):
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
	elif command == 'ak':
		printActions()
	else:
		print('\ninvalid command\n')

def main():
	print('Adventure Game')
	printActions()
	activePlayer = Player(input('enter your player name - '), room['outside'])
	print()

	while True:
		print(activePlayer.currentRoom)

		command = input('enter command for next action - ')

		if (command == 'q') or (command == 'quit'):
			break
		commandParser(command, activePlayer)

main()

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# def commandParser(command, activePlayer):
# 	if command == 'n':
# 		if activePlayer.currentRoom.n_to != None:
# 			return activePlayer.currentRoom.n_to
# 		else:
# 			print('\nthere is no room north of the current room\n')
# 	elif command == 's':
# 		if activePlayer.currentRoom.s_to != None:
# 			return activePlayer.currentRoom.s_to
# 		else:
# 			print('\nthere is no room south of the current room\n')
# 	elif command == 'e':
# 		if activePlayer.currentRoom.e_to != None:
# 			return activePlayer.currentRoom.e_to
# 		else:
# 			print('\nthere is no room east of the current room\n')
# 	elif command == 'w':
# 		if activePlayer.currentRoom.w_to != None:
# 			return activePlayer.currentRoom.w_to
# 		else:
# 			print('\nthere is no room west of the current room\n')
# 	else:
# 		print('invalid command')
#
# def main():
# 	activePlayer = Player(input('enter your player name - '), room['outside'])
#
# 	while True:
# 		print(f'Current Room - {activePlayer.currentRoom}\n')
# 		print(f'Room Description - {room[activePlayer.currentRoom]}\n')
#
# 		command = input('enter command for next action - ')
#
# 		if (command == 'q') or (command == 'quit'):
# 			break
# 		activePlayer.currentRoom = commandParser(command, activePlayer)
#
# main()
