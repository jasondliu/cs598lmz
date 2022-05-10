import _struct
# Test _struct.Struct

p = _struct.Struct('i')
p
p.size
p.format
p.pack(7)
q = _struct.Struct('ii')
q.pack(7, 18)
q.pack([7, 18])
q.pack((7, 18))
# non-int values
q.pack([7.0, 18.0])
# len mismatch
try:
    q.pack(7, 18, 19)
except:
    print("exception as expected")
try:
    q.pack([7, 18, 19])
except:
    print("exception as expected")
try:
    q.pack((7, 18, 19))
except:
    print("exception as expected")
try:
    q.pack(q)
except:
    print("exception as expected")
try:
    q.pack("abc")
except:
    print("exception as expected")
# only one format unit is supported
