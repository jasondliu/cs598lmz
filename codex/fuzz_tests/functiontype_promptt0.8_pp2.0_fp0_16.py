import types
# Test types.FunctionType type
def func1(): pass
isinstance(func1, types.FunctionType)
# Test types.CodeType type
import dis
def func1(): pass
dis.dis(func1)

func1.__code__
isinstance(func1.__code__, types.CodeType)
# Test types.TracebackType type
def func1(): pass
def func2(): pass
def func3(): pass
def func4(): pass

func1()
func2()
func3()
func4()
import sys
import types

def test(frame, event, arg):
    if event == 'call':
        return test
    elif event == 'exception':
        print('function %s raised an exception' % frame.f_code.co_name)
    return

sys.settrace(test)
# test the types
import types
isinstance(func1, types.FunctionType)
isinstance(func1.__code__, types.CodeType)
# isinstance(func1.__code__.co_code, types.TracebackType)
# isinstance
