import types
types.FileType

ftype1 = types.FileType(None, 'o', 'utf-8')

ftype1.read()
ftype1.write('hello world')

ftype2 = types.FileType(None, 'o', 'gbk')
ftype2.write('你好')

import sys
sys.stdout
help(sys.stdout)
sys.stdout
sys.stdout.write('hello')
