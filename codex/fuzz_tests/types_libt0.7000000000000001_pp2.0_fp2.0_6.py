import types
types.FunctionType

# 比较两个函数的相同
# 1.名字相同
# 2.__code__ 相同
# 3.__globals__ 相同
# 4.__closure__ 相同
# 5.__dict__ 相同

def f1():
    pass
def f2():
    pass
def f3():
    pass

def compare(f1,f2):
    return (f1.__name__ == f2.__name__) and (f1.__code__.co_code == f2.__code__.co_code) and \
           (f1.__code__.co_filename == f2.__code__.co_filename) and (f1.__code__.co_argcount == f2.__code__.co_argcount) and \
           (f1.__code__.co_cellvars == f2.__code__.co_cellvars) and (f1.__code
