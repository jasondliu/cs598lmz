from _struct import Struct
s = Struct.__new__(Struct)
# These codes work in Python 3.2 and above:
s.format = 'I 2s f'
s.size = Struct.calcsize(s.format)
print(s.size)

import time, os.path
metafiles = []
for filename in os.listdir('.'):
    if filename.endswith('.meta'): 
        metafiles.append(filename)

metafiles.sort(key=lambda filename: os.path.getmtime(filename))
print(metafiles)        

# Native 
metafiles.sort(key=os.path.getmtime)
print(metafiles)

import bisect
def grade(score, breakpoints=[60,70,80,90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

def deco(func):
    import functools
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('running inner()')
        return
