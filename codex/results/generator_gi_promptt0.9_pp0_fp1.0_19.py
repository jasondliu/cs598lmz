gi = (i for i in ())
# Test gi.gi_code
gi.gi_code


class C:
    pass

# TypeError: 'int' object is not iterable
iter(C)

c = C()
# TypeError: iteration over non-sequence
iter(c)
