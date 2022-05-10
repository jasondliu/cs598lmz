import types
# Test types.FunctionType
def func():
    pass
if type(func) == types.FunctionType:
    print("Yes, it is a function.")

print("------------")

# Test types.LambdaType
func2 = lambda x: x+1
if type(func2) == types.LambdaType:
    print("Yes, func2 is a lambda function.")


# type() function
print("------------")

print(type("Hello, World!"))
print(type(1))
print(type(1.0))
print(type(1+1j))
print(type(1>2))
print(type(lambda x: x+1))
print(type((1,2,3)))
print(type([1,2,3]))
print(type({1,2,3}))
print(type({1:2, 3:4}))
print(type({1:"a", 3:"b"}))
