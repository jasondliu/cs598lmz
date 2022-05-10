from types import FunctionType
a = (x for x in [1])
print(FunctionType(a, globals(), '<mygen>')([2]))

# yield from (2)
# print(list(yield_from_test(4)))

# yield from (3)
# def ptest(param):
#     yield from test(param)
#
# print(list(ptest(4)))
