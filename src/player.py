class Player:
	def __init__(self, name, currentRoom):
		self.name = name
		self.currentRoom = currentRoom
		self.playerItems = []

	def __repr__(self):
		return f'Player Name - {self.name}\nCurrent Room - {self.currentRoom}\nPlayer Items = {self.playerItems}'

	def addItem(self, item):
		self.playerItems.append(item)
		print(f'you picked up - {item}')
