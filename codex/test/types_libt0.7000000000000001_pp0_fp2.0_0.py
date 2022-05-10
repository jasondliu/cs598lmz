import types
types.MethodType(meth, c)

from types import MethodType
MethodType(meth, c)

# 클래스 변수에 메소드 추가
class C: pass

def meth(self, y):
    return self.x + y

c = C()
c.x = 10
c.m = types.MethodType(meth, c)
c.m(11)

# 디스크립터를 이용한 메소드 추가
def meth(self, y):
    return self.x + y

class C: pass
c = C()
c.x = 10

setattr(C, 'm', meth)
c.m(11)

# m 디스크립터 클래스 구현
