from types import FunctionType
list(FunctionType(lambda x:x, globals(), 'lambda'))

# 2.5.5.3.3. 클래스 메서드
# 클래스 메서드는 클래스 자체에 적용되는 메서드이다.
# 클래스 메서드는 첫 번째 인자로 클래스를 받는다.
class C:
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
# 클래스 메서드를 호출할 때는 클래스
