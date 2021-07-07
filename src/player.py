class Player:
	def __init__(self, name, currentRoom):
		self.name = name
		self.currentRoom = currentRoom
		self.playerItems = []

	def __repr__(self):
		return f'Player Name - {self.name}\nCurrent Room - {self.currentRoom}\nPlayer Items = {self.playerItems}'

	def printInventory(self):
		print('\nplayer inventory')
		for item in self.playerItems:
			print(item)
		print()

	def checkMovementCommand(self, direction):
		directionAttr = f'{direction[0]}_to'
		if hasattr(self.currentRoom, directionAttr):
			print(f'\nmoving {direction}...\n')
			self.currentRoom = getattr(self.currentRoom, directionAttr)
		else:
			print(f'\nthere is no room [{direction}] of the current room\n')
			# if command == 'n':
			# 	print('\nthere is no room [north] of the current room\n')
			# elif command == 's':
			# 	print('\nthere is no room [south] of the current room\n')
			# elif command == 'e':
			# 	print('\nthere is no room [east] of the current room\n')
			# elif command == 'w':
			# 	print('\nthere is no room [west] of the current room\n')

	def handleItemCommand(self, playerCommandList):
		command = playerCommandList[0]
		if len(playerCommandList) == 1:
			if command == 'i':
				self.printInventory()
		elif len(playerCommandList) >= 2:
			targetItem = playerCommandList[1]
			if (command == 'get') or (command == 'take'):
				for roomItem in self.currentRoom.roomItems:
					if targetItem in roomItem.name:
						if roomItem.name == targetItem:
							self.addItem(roomItem)
							self.currentRoom.removeItem(roomItem)
							roomItem.onTake()
							return
						else:
							print(f'\nitem - {targetItem} not found, to get an item make sure you type it the same way that it is shown in room items\n')
							return
				print(f'\nitem - {targetItem} not found in current room\n')
			elif command == 'drop':
				for playerItem in self.playerItems:
					if targetItem in playerItem.name:
						if playerItem.name == targetItem:
							self.removeItem(playerItem)
							self.currentRoom.addItem(playerItem)
							playerItem.onDrop()
							return
						else:
							print(f'\nitem - {targetItem} not found, to get an item make sure you type it the same way that it is shown in player inventory\n')
							return
				print(f'\nitem - {targetItem} not found in player inventory\n')

	def addItem(self, item):
		self.playerItems.append(item)

	def removeItem(self, item):
		self.playerItems.remove(item)
