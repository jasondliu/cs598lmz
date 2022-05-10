from types import FunctionType
list(FunctionType(input(), {}).__code__.co_code)
#11,12
