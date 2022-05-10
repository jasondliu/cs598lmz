from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b')
s.pack(1)

# these are the class methods that are invoked
# Struct.__init__
# Struct.__new__
# Struct.pack

import _struct
dir(_struct)
'''

import re

re.findall('\w+$', 'http://www.python.org')

class LazyImport(object):
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, attr_name):
        if self.module is None:
            self.module = __import__(self.module_name)

        return getattr(self.module, attr_name)

import networkx as nx
G = nx.Graph()

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

# nx.write_dot(G, 'test.dot')

#!dot -Tpng test
