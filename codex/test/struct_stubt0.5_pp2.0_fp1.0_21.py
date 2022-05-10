from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'I')
print(s.size)
print(s.pack(17))
print(s.unpack(s.pack(17)))

# 텍스트 인코딩
# 인코딩은 언어에서 사용되는 문자를 컴퓨터 메모리에 저장하는 방법을 말한다.
# 인코딩은 인코딩 방식이라고도 하며, 인코딩 방식은 인코딩 방식의 이름이라고도 
