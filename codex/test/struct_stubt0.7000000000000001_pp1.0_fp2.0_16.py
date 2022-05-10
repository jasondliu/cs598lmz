from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('x')
# TypeError: __init__() takes exactly 2 positional arguments (1 given)

# 특수 메서드는 인스턴스 생성에만 쓰임
# 단순히 생성자를 호출할 때는 object.__new__()와 object.__init__()를 따로 호출해야 함
