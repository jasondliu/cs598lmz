from _struct import Struct
s = Struct.__new__(Struct)
b'{}'.format(s)

class S(object):
    def __format__(self, *args):
        return 'S'

'{}'.format(S())

'{}'.format(S())

'{:b}'.format(42)

'{:0b}'.format(42)

'{:#0b}'.format(42)

'{:10}'.format('hello')

'{:>10}'.format('hello')

'{:^10}'.format('hello')

'{:10}'.format('this is a long string')

'{:*^30}'.format('centered')

'{:*^30}'.format('this is a long string')

'{:*^30}'.format('this is a very long string')

'{0:*^30}'.format('centered')

'{0:*^30}'.format('this is a long string')

'{0:*^30}'.format('this is a very long string')

'
