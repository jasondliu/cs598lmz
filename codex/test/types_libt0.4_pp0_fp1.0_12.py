import types
types.ClassType

# 클래스 생성
class C:
    pass

# 클래스 인스턴스 생성
c = C()

# 인스턴스를 클래스의 인스턴스로 인식
isinstance(c, C)

# 인스턴스를 클래스의 상속받은 클래스의 인스턴스로 인식
isinstance(c, object)

# 인스턴스를 클래스의 상속받은 클래
