from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# list(x for x in range(10))
# list(x for x in range(10) if x % 2)
# list(x for x in range(10) if x % 2 == 0)
# list(x for x in range(10) if x % 2 == 0 if x % 3 == 0)
# list(x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0)
# list(x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0 if x % 7 == 0)
# list(x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0 if x % 7 == 0 if x % 11 == 0)
# list(x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0 if x % 7 == 0 if x % 11 == 0 if x % 13 == 0)
# list(x for
