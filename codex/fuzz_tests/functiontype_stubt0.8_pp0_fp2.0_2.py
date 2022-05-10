from types import FunctionType
a = (x for x in [1])

b = FunctionType(a.gi_code, globals(), 'a')

b()

# 1.4

# 1.5


# 2
# 2.1

print '%c' % 0xFF

# 2.2



# 2.3



# 2.4
