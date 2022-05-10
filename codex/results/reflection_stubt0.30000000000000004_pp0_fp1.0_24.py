fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# __code__ is a read-only attribute

# fn.__code__ = 42
# TypeError: readonly attribute

# fn.__code__ = 'spam'
# TypeError: readonly attribute

# fn.__code__ = b'spam'
# TypeError: readonly attribute

# fn.__code__ = bytearray(b'spam')
# TypeError: readonly attribute

# fn.__code__ = memoryview(b'spam')
# TypeError: readonly attribute

# fn.__code__ = 'spam'.encode('utf-8')
# TypeError: readonly attribute

# fn.__code__ = 'spam'.encode('utf-16')
# TypeError: readonly attribute

# fn.__code__ = 'spam'.encode('utf-32')
# TypeError: readonly attribute

# fn.__code__ = 'spam'.encode('utf-16-le')
# TypeError
