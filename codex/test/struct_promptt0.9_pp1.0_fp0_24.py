import _struct
# Test _struct.Struct class:

s = _struct.Struct('hhl')
for f in ('ihhl', '24s5s'):
    try:
        s.unpack(f)
    except (TypeError, struct.error):
        pass
    else:
        print('failed:', f)

class X(object):

    def __int__(self):
        return 5

    def __index__(self):
        return 6

    def __index__(self):
        return 7

x = X()
print(int(x), int(x), int(x))

obj = list(range(5))
del obj[2]
length = len(obj)
print(length)
obj[-5:] = obj[2:2]
print(len(obj))
del obj[-3:-3]
print(obj)
del obj[-3:-3]
print(len(obj))

del obj[0]
print(len(obj))

del obj[-1]
print(len(obj))

del obj[:]
