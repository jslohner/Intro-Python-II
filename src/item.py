class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __repr__(self):
		return self.name

	def onTake(self):
		print(f'\nyou picked up {self.name}\n')

	def onDrop(self):
		print(f'\nyou dropped {self.name}\n')
