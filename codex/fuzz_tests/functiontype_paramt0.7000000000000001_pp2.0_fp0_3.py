from types import FunctionType
list(FunctionType())

# code: 
# def f(): pass
# list(f)

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'function' object is not iterable
# Explanation:
# Because functions are not iterable, you cannot apply the iter() function on them.
 
# *********************************************************************************************************************

# What is the output of the following code?

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# print(issubclass(B, A))
# print(issubclass(C, B))
# print(issubclass(C, A))

# code: 
# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# print(issubclass(B, A))
# print(issubclass(C, B))
# print(issubclass(C, A))

