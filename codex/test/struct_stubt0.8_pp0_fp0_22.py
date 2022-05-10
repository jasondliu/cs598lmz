from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b')
s.unpack(b'a')

a = {'foo' : 1}
b = {'bar' : 2}
a.update(b)

import collections
collections.ChainMap(a, b)

values = a, b
{k: v for d in values for k, v in d.items()}

with open('example.txt', 'r', encoding='utf-8') as f:
    print(f.read())

for line in f:
    print(line, end='')

def coprocess(in_file, out_file):
    while True:
        data = in_file.readline()
        if not data:
            break
        out_file.write('got:' + data)

coprocess(f, sys.stdout)

import pprint
pprint.pprint(data)

pprint.pprint(data, stream=f)

import logging
logging.debug('Debugging information')
logging.info('Informational message')
log
