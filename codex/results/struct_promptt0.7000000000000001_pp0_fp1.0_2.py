import _struct
# Test _struct.Struct
sizeof( _struct.Struct("x").size )

def test():
    _struct.Struct("@").size

test()

def test():
    _struct.Struct("!").size

test()

def test():
    _struct.Struct("x").size

test()

def test():
    _struct.Struct("!=i").unpack(b"\x00\x00\x00\x01")

test()

def test():
    _struct.Struct("?=i").pack(True)

test()
