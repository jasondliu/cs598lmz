gi = (i for i in ())
# Test gi.gi_code
# (s == "<generator object <genexpr> at 0x7fbccb2f9f0>") is True
# (c == <frozenset>) is True
# (gi.gi_code == None) is True

def main (p):
    gi = p.create_generator_info(func)
    # Test gi.gi_code
    # (s == "<code object func at 0x7fbccb0d1270, file 'cpython/Python/pystate.c', line 31>") is True
    # (c == <frozenset>) is True
    # (gi.gi_code == s) is True

main (p)

print('TEST SUCEEDED')
