from types import FunctionType
a = (x for x in [1])
print(type(a))

def gen():
    a = 1
    while True:
        yield a
        a = yield a + 1


g = gen()
print(type(g))
# print(g.send(None))
# print(g.send(None))
# print(g.send(None))
# print(g.send(None))

class Gen(object):
    def __init__(self):
        self.__num = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__num += 1
        return self.__num + 1

    def send(self, value):
        print('send value %s' % value)
        return self.__next__()

g = Gen()

def test():
    for _ in range(5):
        print(g.send(None))


import itertools
def limit():
    yield from itertools.islice(g.send(None), 2)

test()

import asyncio


async def hello():
