import types
types.SimpleNamespace(ast="a", b="b", c="c")

from collections import namedtuple
MyTuple = namedtuple('MyTuple', ['ast', 'b', 'c'])
my_tuple = MyTuple('a', 'b', 'c')

from collections import OrderedDict
OrderedDict([('ast', 'a'), ('b', 'b'), ('c', 'c')])

from types import SimpleNamespace
dict(SimpleNamespace(**{'ast': 'a', 'b': 'b', 'c': 'c'})._asdict())


&gt;&gt;&gt; d = {'a': 10, 'b':20}

&gt;&gt;&gt; dict(zip([k[0] for k, v in sorted(d.items(), key=lambda x: x[1])], d.values()))

&gt;&gt;&gt; import heapq
&gt;&gt;&gt; heapq.nsmallest(2, d.items(), key=lambda x: x[1])
