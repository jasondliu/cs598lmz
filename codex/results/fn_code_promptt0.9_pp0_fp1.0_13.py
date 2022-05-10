fn = lambda: None
# Test fn.__code__.co_firstlineno 
# def inner():
    # return "10"
# x = inner()
# print(x)

# # Test fn.__code__.co_varnames
# y = '5'
# print( (lambda: y) )

# Test lambda
# f1 = lambda : "return the value"
# f2 = lambda : y
# f1()
# y = '5'
# f2()


# Test sys.getrefcount 
# import sys
# x = 10
# print(sys.getrefcount(x))

# Test gettaer and settaer
# class VerySimple(object):
#     def __init__(self):
#         self.value = 1
#     @property
#     def value(self):
#         return 10
#     @value.setter
#     def value(self, value):
#         self.value = value

# x = VerySimple()
# print(x.value)
# x.value = "16"
# print(x.value)

# Test En
