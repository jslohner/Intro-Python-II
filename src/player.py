class Player:
	def __init__(self, name, currentRoom):
		self.name = name
		self.currentRoom = currentRoom

	def __repr__(self):
		return f'Player Name - {self.name}\nCurrent Room - {self.currentRoom}'
