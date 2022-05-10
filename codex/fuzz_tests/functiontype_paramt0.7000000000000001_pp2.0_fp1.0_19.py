from types import FunctionType
list(FunctionType('a','b','c','d','return d',({},),1))

# test block_stack
#

def f():
    print(1)
    try:
        print(2)
        raise Exception
    finally:
        print(3)
    print(4)

f()

def g():
    print(1)
    try:
        print(2)
        try:
            print(3)
            try:
                print(4)
                return
            finally:
                print(5)
        except Exception:
            print(6)
        print(7)
    finally:
        print(8)
    print(9)

g()

def h():
    print(1)
    try:
        print(2)
        try:
            print(3)
            return
        finally:
            print(4)
    except Exception:
        print(5)
    print(6)

h()

def i():
    print(1)
    try:
        print(2)
        try:
            print(
