from types import FunctionType
list(FunctionType(lambda: 'spam').__code__.co_freevars)

(lambda: 'spam').__code__.co_freevars

def f1():
    x = 88
    def f2():
        print(x)
    return f2

action = f1()
action()

def f1():
    x = 88
    def f2():
        print(x)
    return f2

action = f1()
action()

action.__closure__

action.__closure__[0].cell_contents

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)

F('spam')

F('ham')

F('eggs')

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(0)

