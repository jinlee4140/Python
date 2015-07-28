class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

coor1 = Coordinates(2,3)
print coor1.getX()
print coor1.getY()

coor2 = Coordinates(-5, 15)
print coor2.getX()
print coor2.getY()

