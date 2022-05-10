import types
types.SimpleNamespace(ast="a", b="b", c="c")

from collections import namedtuple
MyTuple = namedtuple('MyTuple', ['ast', 'b', 'c'])
my_tuple = MyTuple('a', 'b', 'c')

from collections import OrderedDict
OrderedDict([('ast', 'a'), ('b', 'b'), ('c', 'c')])

from types import SimpleNamespace
dict(SimpleNamespace(**{'ast': 'a', 'b': 'b', 'c': 'c'})._asdict())


