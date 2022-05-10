from types import FunctionType
list(FunctionType(a.__code__, globals(), "s")())

# 실습 2
class C:
    def sum(self, a, b):
        return a + b
print(globals().get('C').sum(globals()['C'](), 2, 3))

class C:
    def sum(self, a, b):
        return a + b
#print(globals()['C']().sum(globals()['C'](), 1, 2))
#print(globals().get('C')().sum(globals().get('C')(), 1, 2))
print(globals()['C']().sum(globals().get('C')(), 1, 2))


# 클래스 변수
# 실습 1
class C: pass
C.w = 1
I = C()
I.x = 2
print(C.w, I.w, I.x)
I.w = 3
print(C.w
