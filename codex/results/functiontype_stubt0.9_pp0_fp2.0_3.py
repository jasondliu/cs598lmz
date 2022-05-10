from types import FunctionType
a = (x for x in [1])
type(a)

# yield:当做迭代器使用
def test_yield():
    yield 3 # 0
    yield 4 # 1
    yield 5 # 2
    yield 6 # 3
    yield 7 # 4
for x in test_yield():
    print(x)

ks = test_yield()
type(ks)

#for x in test_yield():
#    x = next(test_yield())
#    print(x)



# generator
for x in test_yield():
    yield x




def test_aa(self):
    print('aa')

def test_bb(self, obj1):
    print(self)
    print(obj1)

test_aa(FunctionType(test_bb, (), {}))
