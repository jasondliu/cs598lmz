import codecs
# Test codecs.register_error()

# This should create a LookupError
codecs.register_error("test.lookuperror", lambda x: (u"", x))

# This should create a TypeError
codecs.register_error("test.typeerror", lambda x, y: (u"", x))

# This should create a ValueError
codecs.register_error("test.valueerror", lambda x, y, z: (u"", x))

# This should create a LookupError
