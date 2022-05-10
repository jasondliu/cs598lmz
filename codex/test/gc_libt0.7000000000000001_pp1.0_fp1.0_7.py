import gc, weakref

def func():
    pass

class MyClass:
    def __del__(self):
        print('MyClass.__del__')
    def __call__(self):
        pass
    def __eq__(self, other):
        return True
    def __len__(self):
        return 20
    def __getitem__(self, key):
        return key
    def __lt__(self, other):
        return True
    def __add__(self, other):
        return other

m1 = MyClass()
m2 = MyClass()
m2()

print(m1 == m2)
print(m1 < m2)
l = [1, 2, 3]
print(m1 + l)
print(len(m1))
print(m1[10])

d1 = weakref.WeakValueDictionary()
d1[1] = m1
print(d1[1])

m1_id = id(m1)
del m1
print(gc.collect())
