gi = (i for i in ())
# Test gi.gi_code, gi.gi_weakreflist
gi.gi_code = 42
gi.gi_weakreflist = 42
# Test gi.next()
gi.next()

# Test where type has buffer interface
int_value = 42
bi_gi = (i for i in buffer(bytearray(b"hello")))
# Test gi.gi_frame
bi_gi.gi_frame = 42
# Test gi.gi_code
bi_gi.gi_code = 42
# Test gi.gi_weakreflist
bi_gi.gi_weakreflist = 42
# Test gi.next()
bi_gi.next()

# Standalone function to test function attributes at module level
# (just globals)
def generator_attribute_func():
    pass
generator_attribute_func.__name__ = 42
generator_attribute_func.__doc__ = 42
generator_attribute_func.__module__ = 42
generator_attribute_func.__defaults__ = 42
generator_attribute_func.__code__ = 42

