from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add1')(1))

# 파이썬은 함수를 인자로 받거나 함수를 반환하는 함수를 지원한다.
# 이러한 함수를 고차함수(higher-order function)라고 한다.
# 인자로 함수를 받는 함수를 인자를 받는 함수라고 하고
# 반환값으로 함수를 반환하는 함
