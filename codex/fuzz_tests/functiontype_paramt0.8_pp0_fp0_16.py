from types import FunctionType
list(FunctionType(1, 2, 3, 4, 5, 6, 7))

# codeobj.co_flags

# codeobj.co_freevars

# codeobj.co_name

# codeobj.co_names

# codeobj.co_nlocals

# codeobj.co_stacksize
# codeobj.co_varnames

# (2, 3, 4, 5, 6, 7)
# 4
# 4
# 1
# 4
# (1, 2, 3, 4, 5, 6, 7)
# 7
# 0
# 6


def example(self):
    if self:
        def func(self):
            pass
        pass
    pass


codeobj = example.__code__

print(codeobj.co_argcount, codeobj.co_nlocals)
print(codeobj.co_cellvars, codeobj.co_freevars)

# 2 4
# () ()
