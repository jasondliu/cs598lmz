from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>h')
s.pack(1)

class Struct(Struct):
    def __call__(self, *args):
        return self.pack(*args)

s = Struct('>h')
s(1)

import operator
operator.__add__(1, 2)

operator.add(1, 2)

operator.add(['a', 'b'], ['c', 'd'])

operator.add('a', 'b')

operator.add(1, 2)

operator.add(1.0, 2.0)

operator.add(1.0, 2)

operator.add(1, 2.0)

operator.add(1j, 2j)

operator.add(1j, 2)

operator.add(1+2j, 3)

operator.add(1+2j, 3j)

operator.add('a', 'b')

operator.add('a', 'b')

operator.add('a', 'b')

operator.add('a', '
