from _struct import Struct
s = Struct.__new__(Struct)
#note that the first argument must be a single non-whitespace character
s.pack("<H", 5)

#The same thing is available with unpack
s.unpack("<h", "A")

#Format strings pass in arguments as they are given
print("Hello {}".format(3))
print("Hello {0}, hello {1}".format(3, "me"))
print("Hello {1}, hello {0}".format(3, "me"))
print("Hello {name}, hello {number}".format(number = 3, name = "me"))

p = [4, "meow"]
print("Hello {0[0]}, hello {1[1]}".format(p, p))

#Another way to do the same
print("Hello {0}, hello {1}".format(*tuple(p)))

#And another way
print("Hello ", "".join(map(str, p)))

#Note that format will try to be smart about argument types
print("Hello {0:x}".format(255))
print("Hello {0:o}".format
