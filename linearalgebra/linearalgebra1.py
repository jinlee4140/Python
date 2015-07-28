from numpy import array
a1 = array([1, 1, 1])
a2 = array([1, 2, 3])
print a1 + a2


a3 = []
for i in range(len(a1)):
	a3.append(a1[i] + a2[i])
print a3

a3 = [a1[i] + a2[i] for i in range(len(a1))]
print a3

print a1 * 2
print a1 * a2
print a2 ** 2

a1 = array((1, 2, 3))
print a1[0]
print a1[1:]
print type(a1)
print type(a1[1:])

#Multi-dimensional array
am = array([[1, 2, 3], [4, 5, 6]])
am[0]
am[0][1]