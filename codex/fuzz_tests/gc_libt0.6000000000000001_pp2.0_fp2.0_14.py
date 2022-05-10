import gc, weakref

class C:
    def __del__(self):
        print("C.__del__")

c1 = C()
c2 = c1

print("c1:", c1)
print("c2:", c2)

# del c1
# print("c1:", c1)
# print("c2:", c2)

def bye():
    print("Gone with the wind...")

ender = weakref.finalize(c1, bye)
print(ender.alive)
del c1
print(ender.alive)
del c2
print(ender.alive)

gc.collect()
print(ender.alive)
