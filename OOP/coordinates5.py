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

	def __eq__(self, coordinates2):
		if self.x == coordinates2.x and self.y == coordinates2.y:
			return True
		else:
			return False

	def __add__(self, object2):
		return Coordinates(self.x + object2.x, self.y + object2.y)

coor1 = Coordinates(2, 3)
coor2 = Coordinates(4, 5)
coor3 = Coordinates(2.0, 3.0)
print coor1.__str__()
print coor1.__eq__(coor2)
print coor1.__eq__(coor3)

print coor1.__add__(coor2)
print coor1
print type(coor1)
print isinstance(coor1, Coordinates)
print isinstance(1, Coordinates)
#What exactly does isinstance method do?

print coor1 + coor2

#when + is used between two objects, the __add__ method is called. 
#coor3 = coor1 + coor2 is equivalent to coor1.__add__(coor2)