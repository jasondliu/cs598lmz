import types
types.FunctionType
 
#클래스 형태로 정의한 함수

def class_func():
    pass
class_func.__class__

#함수의 비교
def func1():
    pass
def func2():
    pass
func1 == func2

def func1():
    pass
def func1():
    pass
# func1 == func1 # 오류가 난다.

#함수의 주소가 바뀌는 것을 막기위해서는 함수의 주소를 변수에 저장해서 사용한다.
a = func1
a
a == func1
#func1의 주
