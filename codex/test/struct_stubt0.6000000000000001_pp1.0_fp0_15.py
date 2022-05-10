from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab', 2.7)

from operator import itemgetter, attrgetter, methodcaller
itemgetter(1)('ABCDEFG')
itemgetter(1, 3, 5)('ABCDEFG')
attrgetter('sort')(list)
attrgetter('name')(s)
attrgetter('shares', 'price')(s)
methodcaller('replace', 'l', 'L')('Hello World')

from itertools import *
list(chain('ABC', 'DEF'))
list(chain.from_iterable(['ABC', 'DEF']))
list(compress('ABCDEF', [1, 0, 1, 0, 1, 1]))
list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
list(filterfalse(lambda x: x % 2, range(10)))
list(islice('ABCDEFG', 2))
list(islice('ABCDEFG', 2, 4))
