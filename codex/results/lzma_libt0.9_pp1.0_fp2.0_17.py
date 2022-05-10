import lzma
lzma.open('*.lzma')
XZ File ('*.lzma') : 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
test("""\
open(name)
Open a file using the file() type, returns a file object.  This is the
preferred way to open a file.  See file.__doc__ for further information.
""")

# imp.reload
reload = test("""\
doctest for __builtin__.reload
>>> import sys, imp
>>> m = sys.modules.copy()
>>> imp.reload(sys) # does nothing; sys is already loaded
>>> imp.reload(sys) # does nothing; sys is already loaded
>>> sys.modules == m
True
>>> import string
>>> m = sys.modules.copy()
>>> imp.reload(string)
<module 'string' from '...lib...string.pyc'>
>>> sys.modules == m # doctest: +SKIP
True
>>> # Now change string
>>> string.foo = 1
>>> imp.reload(string)
<module 'string' from '...
