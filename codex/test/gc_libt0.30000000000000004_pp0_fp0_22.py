import gc, weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass({!r})'.format(self.name)

o = MyClass('instance')
r = weakref.ref(o)
print(r)
print(r())
print(o)
del o
print(r())
print(gc.collect())
print(r())

print('-' * 20)

s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)

print('-' * 20)

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print
