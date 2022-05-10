import _struct
# Test _struct.Struct.__sizeof__


class S(_struct.Struct):
    _fmt = "<17p"


assert S.__sizeof__() == 17 * _struct.calcsize('p')
