import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    print(m[:])
    m.close()
    print(f.read())

import re

re.findall(r'\d+', '1a2b3c')

import os

os.path.join('/home/user', 'a', 'b')

import time

time.time()
time.sleep(1)
time.time()

import math

math.ceil(3.14)
math.floor(3.14)

import random

random.random()

random.randint(0, 10)

random.randrange(1, 10)

random.choice([1, 2, 3])

random.sample([1, 2, 3], 2)

random.shuffle([1, 2, 3])

import datetime

d = datetime.date(2020, 1, 1)

d.year
d.month
d.day

t = datetime.time(12, 34, 56)

t.hour
t.minute
