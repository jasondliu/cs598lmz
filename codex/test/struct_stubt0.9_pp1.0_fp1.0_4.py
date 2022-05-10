from _struct import Struct
s = Struct.__new__(Struct)
# Initialize it
s.__init__('10s h')

class Person:
	def __init__(self, buf):
		data = s.unpack(buf)
		self.fn = data[0]
		self.age = data[1]
	def __str__(self):
		return '%s(%s)' % (self.fn.strip(b'\x00').decode('utf8'), self.age)

with open('data2.bin', 'rb') as f:
	buf = f.read()

people = []
for p in range(0, len(buf), s.size):
	people.append(Person(buf[p:p+s.size]))

for p in people:
	print("Person: {}".format(p))
