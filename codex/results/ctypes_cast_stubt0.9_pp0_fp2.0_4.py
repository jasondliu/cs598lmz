import ctypes
ctypes.cast(ll, ctypes.py_object).value

sorted(ll, key=lambda x: x)
#could need to * 2 to len.
idx = 2 * len(ll)
for n in ll:
	print('%d -> %d' % (n, idx))

a = [(x,y) for x in range(11) for y in range(11) ]
a
a = [[] for x in range(11)]
a = []
for x in range(11):
	z = []
	for y in range(11):
		a.append((x,y))
		z.append(None)
	a.append(z)
#18.1
import bisect
class Gradebook(object):
	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True

	def add_student(self, student):
		if student in self.students:
			raise ValueError('Duplicate Student')

		self.students.append
