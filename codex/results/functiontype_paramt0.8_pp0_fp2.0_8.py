from types import FunctionType
list(FunctionType(lambda x: print(x), globals(), 'test') for x in range(2))

# # SyntaxError: 'return' with argument inside generator
return 1

# # SyntaxError: invalid syntax
# SyntaxError: unexpected EOF while parsing
lambda x, y=1: x
lambda x, y=1: x return x
lambda x, y=1: x * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19

# print(sorted(globals().keys()))
