import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

# 10
# 10

# WeakValueDictionary 객체는 값이 참조되고 있는 동안에만 유효하다.
# 참조되고 있지 않은 값은 자동으로 제거된다.
# 이런 점을 이용하면 객체를 캐
