import ctypes
ctypes.cast(1000, ctypes.py_object).value

#9
def my_func():
    try:
        return 1
    finally:
        return 2
my_func()

#10
def my_func():
    try:
        return 'from_try'
    except ValueError:
        return 'from_except'
my_func()

#11
def my_func():
    try:
        raise ValueError()
    except ValueError:
        return 'from_except'
my_func()

#12
def my_func():
    try:
        raise ValueError()
    except:
        return 'from_except'
    else:
        return 'from_else'
my_func()

#13
def my_func():
    try:
        1/0
    finally:
        return 'from_finally'
my_func()

#14
def my_func():
    try:
        1/0
    except:
        return 'from_except'
    else:
        return 'from_else'
    finally:

