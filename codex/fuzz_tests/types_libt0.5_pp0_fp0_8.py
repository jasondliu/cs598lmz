import types
types.MethodType(lambda self, x: x, None)

class A(object):
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

a = A(1)
a(1)

class B(object):
    def __init__(self):
        self.x = 1
    def __call__(self, y):
        return self.x + y

b = B()
b(1)

b.x = 2
b(1)

# __call__() 의 장점
# 1. 인스턴스를 함수처럼 호출할 수 있다.
# 2. 다른 함수에 인스턴스를 전달할 수 있다.
def plus_one(
