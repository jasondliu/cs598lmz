from types import FunctionType
list(FunctionType(a,b,c).__dict__.keys())

# code ------------ none
# co_consts ------------ ('hi',)
# co_filename ------------ ('./test.py')
# co_freevars ------------ ()
# co_name ------------ ('x')
# co_nlocals ------------ (0,)
# co_stacksize ------------ (2,)
# co_varnames ------------ ()


"""
FunctionType.func_closure
"""
def x(): pass
# print x.func_closure

"""
FunctionType.func_code
"""
# print x.func_code


"""
FunctionType.func_defaults
"""
def x(a=4): pass
# print x.func_defaults


"""
FunctionType.func_dict
"""
def x(): pass
# print list(x.func_dict.keys())


"""
FunctionType.func_doc
"""
def x(): pass
# print x.func_doc

"""
FunctionType.func_globals
"""
def x(): pass
# print x.func
