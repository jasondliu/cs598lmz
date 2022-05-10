from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.pack(1)

# __new__ is a class method, so it is called on the class, not on an instance.
# The first argument is the class itself.
# The second argument is the string format.
# The third argument is the format character size.
# The fourth argument is the format alignment.
# The fifth argument is the format native size.
# The sixth argument is the format is unsigned flag.

# The __init__ method is called on the instance.
# The first argument is the instance itself.
# The second argument is the string format.
# The third argument is the format character size.
# The fourth argument is the format alignment.
# The fifth argument is the format native size.
# The sixth argument is the format is unsigned flag.

# The pack method is called on the instance.
# The first argument is the instance itself.
# The second argument is the value to pack.

# The unpack method is called on the instance.
# The first argument is the instance itself.
# The second argument is the string to unpack.

# The un
