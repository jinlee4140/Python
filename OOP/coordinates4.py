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

	def __eq__(self, newcoordinate):
		if self.x == newcoordinate.x and self.y == newcoordinate.y:
			return True
		else:
			return False


coor1 = Coordinates(2, 3)
coor2 = Coordinates(4, 5)

coor3 = Coordinates(2.0, 3.0)

coor4 = Coordinates(4.0, 5.0)

print coor1.__eq__(coor2)
print coor1.__eq__(Coordinates(2, 3))
print coor1.__eq__(coor3)