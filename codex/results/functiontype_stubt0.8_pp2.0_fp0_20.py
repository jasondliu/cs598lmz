from types import FunctionType
a = (x for x in [1])
print(isinstance(a,FunctionType))
print(isinstance(a,GeneratorType))
print(type(a) == types.GeneratorType)

import re
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
    print('ok')

test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('failed')

if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
    print('ok')
else:
    print('failed')

if re.match(r'^\d{3}\-\d{3,8}$','010 12345'):
    print('ok')
else:
    print('failed')


print('a b   c'.split(' '))
print(re.split(r'\s+','a
