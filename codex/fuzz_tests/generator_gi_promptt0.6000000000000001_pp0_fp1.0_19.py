gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_name)
# Test gi.gi_frame
print(gi.gi_frame.f_lasti)

# Test tuple.__new__
print(tuple.__new__(tuple))
print(tuple.__new__(tuple, 'abc'))
print(tuple.__new__(tuple, 'abcdef'))
print(tuple.__new__(tuple, 'abcdefghi'))
print(tuple.__new__(tuple, 'abcdefghijklmnopqrstuvwxyz'))
print(tuple.__new__(tuple, 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
# Test tuple.__init__
t = tuple()
t.__init__('abcdefghijklmnopqrstuvwxyz')
print(t)

# Test tuple.__ge__
print((1, 2) >= (1, 2))
print((1, 2
