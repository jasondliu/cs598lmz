from types import FunctionType
list(FunctionType(myfun.__code__, myfun.__globals__, myfun.__name__, myfun.__defaults__, myfun.__closure__))

# print(list(FunctionType(myfun.__code__, myfun.__globals__, myfun.__name__, myfun.__defaults__, myfun.__closure__)))

list((myfun))
