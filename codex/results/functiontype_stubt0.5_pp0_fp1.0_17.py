from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(FunctionType(a) is FunctionType(b))

# 2
print("2")
print(FunctionType(a) == FunctionType(b))

# 3
print("3")
print(FunctionType(a)(1))

# 4
print("4")
print(FunctionType(b)(1))

# 5
print("5")
print(FunctionType(a)(2))

# 6
print("6")
print(FunctionType(b)(2))

# 7
print("7")
print(FunctionType(a)(1))

# 8
print("8")
print(FunctionType(b)(1))

# 9
print("9")
print(FunctionType(a)(1))

# 10
print("10")
print(FunctionType(b)(1))

# 11
print("11")
print(FunctionType(a)(3))

# 12
print("12")
print(FunctionType(b)(3))
