from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
s.format = 'ifi'
s.size = s.calcsize(s.format)
s.pack(b'raymond   ', 80, 0x12345678)

# _asdict converts a named tuple to an ordered dictionary
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# namedtuple unpacking
r = 0, 1, 2, 3, 4
r
r[2]
r[2:4]
r[-3:]

# tuple packing
t = tuple(range(3))
t

len(t)

t[2]

# nested tuple unpacking
latitude, longitude = lax_coordinates
latitude
longitude

# swapping variables
a, b = 1, 2
a, b

b, a = a, b
b, a

# tuple packing and sequence unpacking
divmod(20, 8)

t = (
