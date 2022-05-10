import _struct
# Test _struct.Struct object.
St = _struct.Struct("h")
bytes(b'\xff\xff')

St.pack("-1")

St.unpack("-1")

St.calcsize()

St.format

# Subclassing
class MyStr(str):
    pass

st = MyStr("abc")
st in b'abc '
