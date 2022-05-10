import _struct
# Test _struct.Struct
assert (_struct.calcsize('H')) == (2)
assert (_struct.calcsize('3s4p8s')) == (16)
assert (_struct.calcsize('153p')) == (153)
assert (_struct.calcsize('P')) == (_struct.calcsize('I'))
assert (_struct.calcsize('Pii')) == ((2 * (_struct.calcsize('I'))))

assert (_struct.calcsize('784s')) == (784)
assert (_struct.calcsize('i')) == (4)
assert (_struct.calcsize('f')) == (4)
assert (_struct.calcsize('d')) == (8)
assert (_struct.calcsize('?')) == (1)
assert (_struct.calcsize('b')) == (1)
assert (_struct.calcsize('BB')) == (2)
assert (_struct.calcsize('HH')) == (4)
assert (_struct.calcsize('II')) == (8)
assert (_struct.calcs
