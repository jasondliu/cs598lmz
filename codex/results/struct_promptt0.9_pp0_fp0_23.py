import _struct
# Test _struct.Struct when module is not frozen
p = _struct.Struct('hhc').pack(1, 2, '3')
assert _struct.Struct('hhc').unpack(p) == (1, 2, '3')
print "done (1)"

# Test _struct.Struct when module is frozen
raise SystemExit

p = _struct.Struct('hhc').pack(1, 2, '3')
assert _struct.Struct('hhc').unpack(p) == (1, 2, '3')
print "done (2)"
