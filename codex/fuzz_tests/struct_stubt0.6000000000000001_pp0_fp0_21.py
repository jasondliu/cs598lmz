from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.__init__("i")
s.pack(1)
s.pack(2)
s.pack(4)
s.pack(8)

# The struct module uses a cache for the Struct objects it creates. If we
# create a Struct object directly, it is not added to the cache. This can
# cause problems if we create a Struct object with the same format string as
# another object, but the format string is not interned.

# Create a Struct object with a non-interned format string.
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.__init__("i")

# Create a Struct object with the same format string.
s2 = Struct("i")

# The two objects are different.
s is s2

# The two objects have different format strings.
s.format == s2.format

# The two objects have different format codes.
s.format_code == s2.format_code

# The two objects can
