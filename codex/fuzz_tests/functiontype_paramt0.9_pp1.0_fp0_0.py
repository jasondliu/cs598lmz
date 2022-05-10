from types import FunctionType
list(FunctionType(lambda: x) for x in range(3))
# [<function FunctionType.__init__.<locals>.<lambda> at 0x10b132730>,
# <function FunctionType.__init__.<locals>.<lambda> at 0x10b132dc8>,
# <function FunctionType.__init__.<locals>.<lambda> at 0x10b132378>]


from dis import dis
dis(lambda: x)
#  1           0 LOAD_DEREF               0 (x)
#              2 RETURN_VALUE


def get_functions():
    for i in range(3):
        print('Looking for function for i={}'.format(i))
        yield lambda: i

if __name__ == '__main__':
    for f in get_functions():
        print(f())
