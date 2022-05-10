import types
types.ClassType

# 클래스 생성
class MyClass:
    pass

# 인스턴스 생성
my_instance = MyClass()

# 인스턴스 속성 생성
my_instance.name = '이름'
my_instance.age = '나이'

# 인스턴스 속성 접근
print(my_instance.name)
print(my_instance.age)

# 인스턴스 속성 삭제
del my_instance.name
del my_instance.age

# 인스턴스 속성 접근
print(my_instance.name)
print(my_instance.age)

# 클래
