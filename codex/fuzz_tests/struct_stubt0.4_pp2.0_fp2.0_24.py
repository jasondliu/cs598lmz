from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

import os
os.path.abspath('.')
os.path.abspath('..')
os.path.isabs(os.path.abspath('.'))
os.path.isabs(os.path.abspath('..'))
os.path.isabs('/big/fake/name')
os.path.isabs('big/fake/name/without/a/leading/slash')
os.path.relpath('/a/b/c/d', '/a/b')
os.path.relpath('/a/b/c/d', '/a/b/c')
os.path.relpath('/a/b/c/d')
os.path.relpath('/a/b/c/d', '/a/b/c/d/e')
os.path.relpath('/a/b/c/d/e', '/a/b/c/d')
os.path.relpath('/a/b/c/d/e', '/a
