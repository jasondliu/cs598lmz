from types import FunctionType
a = (x for x in [1])
print(callable(a))
print(isinstance(a, FunctionType))

import re

p = re.compile('\d+')
m = p.match('one12twothree34four')
print(m.group())

print(m.start(0))
print(m.end(0))
print(m.span(0))

print(m.group(1))
print(m.span(1))

s = '<html><head><title>Title</title>'
print(len(s))

s = s.replace('<', '[')
s = s.repalce('>', ']')
print(s)

import re

print(re.findall(r'\d+', 'one1two2three3four4'))

pattern = re.compile(r'\d+')
print(pattern.findall('one1two2three3four4'))

for m in re.finditer(r'\d+', 'one1two2three3four4'):
    print(m
