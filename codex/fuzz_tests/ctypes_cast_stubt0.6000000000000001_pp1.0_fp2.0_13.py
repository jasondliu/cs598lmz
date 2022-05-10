import ctypes
ctypes.cast(1, ctypes.py_object)

# @save
# def mul(a, b):
#     return a * b
# mul.__code__.co_consts

# mul.__code__.co_code
# mul.__code__.co_varnames

# @save
# def add(a, b):
#     return a + b
# add.__code__.co_consts

# add.__code__.co_code
# add.__code__.co_varnames

# def make_adder(a):
#     def adder(b):
#         return a + b
#     return adder
# adder = make_adder(23)
# adder(42)

# adder.__code__.co_freevars
# adder.__closure__

# class Averager():
#     def __init__(self):
#         self.series = []

#     def __call__(self, new_value):
#         self.series.append(new_value)
#        
