import bz2
bz2File = bz2.BZ2File('example.txt.bz2')
bz2File.read()

# file-like objects work with json.dump() and json.load()
import json
json.dump(x, open('data.json', 'w'))
json.load(open('data.json', 'r'))

# Pure json cannot encode custom objects
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
p = Point(1, 2)
json.dumps(p)

# encode custom objects using a function that knows how to convert the object
def serialize_point(point):
	return {'x': point.x, 'y': point.y}
json.dumps(p, default=serialize_point)

# encode all custom objects defined in the same module
import json
def encode_complex(z):
	if isinstance(z, complex):
		return [z.real, z.imag]
	else:
		type_name = z
