from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 파이썬에서는 이런 접근을 허용하지 않는다.
# s.format

# 파이썬은 인스턴스의 프로퍼티를 직접 접근하는 것을 허용하지 않는다.
# 그러나 인스턴스의 프로퍼티를 직접 접근하는 것은 종종 유용하다.
# 파이썬
