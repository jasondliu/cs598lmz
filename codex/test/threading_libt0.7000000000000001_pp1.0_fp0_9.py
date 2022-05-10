import threading
threading.Thread(target=lambda:print(1)).start()

def lambda_test1():
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10))
    print(b(10))

def lambda_test2():
    funcs = [lambda x: x+n for n in range(5)]
    for f in funcs:
        print(f(0))

def lambda_test3():
    funcs = [lambda x, n=n: x+n for n in range(5)]
    for f in funcs:
        print(f(0))

def lambda_test4():
    a = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
    print(a(1, 2, y=3, key='value'))

def lambda_test5():
    args = (1, 2, 3, 4)
    kwargs = {'x': 99}
    a
