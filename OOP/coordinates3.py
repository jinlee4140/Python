class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x 

	def getY(self):
		return self.y

	def __str__(self):
		return '<' + str(self.x) + ',' + str(self.y) + '>'


coor1 = Coordinates(2, 3)
print coor1.__str__()
print coor1

#why are these the same thing? For the second one, I'm not
#passing any method but it'll still print out __str__()
