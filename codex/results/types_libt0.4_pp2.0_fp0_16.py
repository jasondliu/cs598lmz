import types
types.ClassType

# 클래스 정의
class MyClass:
    pass

# 객체 생성
obj = MyClass()

# 클래스 속성
obj.name = "MyClass"
print(obj.name)

# 클래스 메서드
def my_method(self):
    print("my_method")

obj.my_method = types.MethodType(my_method, obj)
obj.my_method()

# 클래스 상속
class MyClass2(MyClass):
    pass

obj2 = MyClass2()
obj2.name = "MyClass2"
print(obj2.name)

# 메서드 오버라이딩
def my_method2(self):
    print("my_method2")

obj
