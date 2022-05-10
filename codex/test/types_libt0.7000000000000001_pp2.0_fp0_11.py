import types
types.FunctionType

# 함수를 클래스의 인스턴스로 만들 수 있다.
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial
fact
fact(5)

# 다음과 같이 인스턴스의 __call__ 메서드를 정의하면 그 인스턴스는 함수처럼 동작한다.
class Factorial:
    def __call__(self, n):
        if n < 2:
            return 1
        return n * self.__call__(n-1)

fact = Factorial()
fact
fact
