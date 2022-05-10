from types import FunctionType
list(FunctionType(lambda: 1, globals(), 'lambda'))
"""

# from types import FunctionType
# list(FunctionType(lambda: 1, globals(), 'lambda'))

def foo():
    try:
        raise Exception()
    except Exception:
        return 1
    finally:
        return 2

# foo()

# class A:
#     def __init__(self):
#         self.name = 'A'

#     def __repr__(self):
#         return self.name

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.name = 'B'

#     def __repr__(self):
#         return super().__repr__()

# B()

# class A:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return self.name

# class B(A):
#     def __init__(self):
#         super().__init
