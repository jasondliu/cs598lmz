from types import FunctionType
list(FunctionType(list(FunctionType.__dict__.values())[0], globals())(0))

# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
