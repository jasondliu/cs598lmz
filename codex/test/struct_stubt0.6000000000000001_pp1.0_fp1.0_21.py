from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<h")

class ShortInt(object):
    __slots__ = ("_value",)
    def __init__(self, value=0):
        if not isinstance(value, (int, long)):
            raise TypeError("Bad argument type for built-in operation")
        self._value = value

    def __repr__(self):
        return str(self._value)

    def __str__(self):
        return str(self._value)

    def __int__(self):
        return self._value

    def __long__(self):
        return self._value

    def __float__(self):
        return float(self._value)

    def __oct__(self):
        return oct(self._value)

    def __hex__(self):
        return hex(self._value)

    def __index__(self):
        return self._value

    def __coerce__(self, other):
        if isinstance(other, (int, long)):
            return self._value, other
