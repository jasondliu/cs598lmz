from types import FunctionType
a = (x for x in [1])
print(isinstance(a,FunctionType))
b = [x for x in [1]]
print(isinstance(b,FunctionType))

a = (x for x in [1])
for i in a:
    print(i)

#功能完全一样
def t(a):
    while True:
        try:
            yield a
            a += 1
        except:
            print('gadad')
            raise
a = t(2)
for i in a:
    print(i)
    if i==4:
        a.throw(Exception)
        break
