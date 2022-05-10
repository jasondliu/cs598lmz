from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# 파이썬의 객체는 모두 속성을 가지고 있다.
# 속성은 객체를 설명하는 데이터를 저장하는 공간이다.
# 속성은 객체에 저장된 데이터를 읽고 쓰는데 사용한다.
# 속성은 객체에 저장된 데이터를 읽고 쓰는데 사
