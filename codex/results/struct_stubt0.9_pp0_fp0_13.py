from _struct import Struct
s = Struct.__new__(Struct)

s.format = 'hi'

print s.pack_into('hello world', 0, 1, 2)  # gets 2 bytes, 1 short
print s.unpack_from('hello world', 0)  # returns a tuple containing 1, 2

# use a Struct subclass to have an extra attribute
class MyStruct(Struct): 
  # add an attribute 'name' to the class
  name = "this is a name"
# create an instance of the subclass
s = MyStruct('hi')
print s.name  # will print "this is a name"

# using the format string, pack a number and a string
f = Struct('i 5s')
print
print f.pack(1, 'hell')
# unpack the data packed before
print f.unpack(f.pack(1, 'hell'))  # will print (1, 'hello')
