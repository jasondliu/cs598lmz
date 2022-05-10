import _struct
# Test _struct.Struct's method of producing a size estimate.
#
# >>> p = _struct.Struct('i')
#
# >>> p.size
# 4
#
# >>> p.size = 42
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: readonly attribute
#
# >>> _struct.error
# 'size cannot be set in this way'
try:
    p = _struct.Struct('i')
except _struct.error:
    print('SKIP')
    raise SystemExit

print(p.size)

try:
    p.size = 42
except AttributeError:
    print('AttributeError: readonly attribute')
