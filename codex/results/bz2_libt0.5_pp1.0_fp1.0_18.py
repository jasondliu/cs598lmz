import bz2
bz2.BZ2File('../data/test.json.bz2').readline()

import json
line = [json.loads(x) for x in bz2.BZ2File('../data/test.json.bz2').readlines()]
print(len(line))
print(line[0])

# bz2.BZ2File('../data/test.json.bz2').readline()

f = bz2.BZ2File('../data/test.json.bz2')
for i in range(5):
    print(f.readline())

import json
line = [json.loads(x) for x in bz2.BZ2File('../data/test.json.bz2').readlines()]
print(len(line))
print(line[0])

# bz2.BZ2File('../data/test.json.bz2').readline()

f = bz2.BZ2File('../data/test.json.bz2')
for i in range(5):
