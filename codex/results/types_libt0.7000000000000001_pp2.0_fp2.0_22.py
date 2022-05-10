import types
types.FunctionType
# FunctionType은 함수를 나타낸다
# types.BuiltinFunctionType은 내장함수를 나타냄
print(type(sum))
print(type(abs))
print(type(lambda x:x))
print(type(x for x in range(10)))
# x for x in range(10)은 generator를 나타냄

# 이름 공간을 지정하여 사용하는 것을 클로저(Closures)라고 한다
def outer():
    x = 1
    def inner():
        print(x)
    inner()
# inner 내부에 x를 받아와 사용한다
# outer
