from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 3.10.2.2 파이썬 객체에 메소드 추가하기

# 파이썬은 언어 자체에 클래스를 지원하지 않는다.
# 클래스도 그저 파이썬의 일반 객체일 뿐이다.
# 파이썬 내장 타입은 기본적으로 새로운 속성을 추가할 수 있
