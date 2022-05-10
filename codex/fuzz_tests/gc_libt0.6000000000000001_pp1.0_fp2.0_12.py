import gc, weakref

class MyObj:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<MyObj {self.name}>"

m = MyObj('mike')

ref = weakref.ref(m)
print(ref)
print(ref())
print(ref() is m)

m = None
print(ref())

gc.collect()
print(ref())

# <weakref at 0x7fbe2bbc4700; to 'MyObj' at 0x7fbe2bbc4c40>
# <MyObj mike>
# True
# <MyObj mike>
# <MyObj mike>
# None
