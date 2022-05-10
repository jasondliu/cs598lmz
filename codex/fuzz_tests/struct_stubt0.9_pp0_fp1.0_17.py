from _struct import Struct
s = Struct.__new__(Struct)

# Fake arguments we pass to Struct().
# Add "s" (representing `Struct`) and "a" (representing `self`) to args
args = ["s", "<p8p8p8p8p8p8p8p8", "a"]
s.__init__(s, *args)

# We add the magic ints to the variables the `Struct` expected to receive
s.s = 42
s.s = 42
s.s = 42
s.s = 42
s.s = 42
s.s = 42
s.s = 42
s.s = 42
s.s = 42

# We call the function (that is inside Struct) which has the vtable as its first argument
s.unpack("H"*16)

# Return
