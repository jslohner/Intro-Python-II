class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.roomItems = []

	def __repr__(self):
		return f'Current Room Name - {self.name}\nCurrent Room Description - {self.description}\nCurrent Room Items - {self.roomItems}'

	def addItem(self, item):
		self.roomItems.append(item)

	def removeItem(self, item):
		self.roomItems.remove(item)
