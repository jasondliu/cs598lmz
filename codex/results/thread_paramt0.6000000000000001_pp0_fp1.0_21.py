import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(sorted(map(str,range(100000))))+'\n')).start()

# a = [1,2,3,4,5]
# a.sort(reverse=True)
# print(a)

# def func():
#     print('hello')
#     print('world')
# func()

# def func1(name):
#     print('hello', name)
# func1('world')

# def func2(name, msg='hello'):
#     print(msg, name)
# func2('world', msg='hi')

# def func3(*args):
#     print(args)
# func3(1,2,3,4)

# def func4(**kwargs):
#     print(kwargs)
# func4(name='world', msg='hello')

# def func5(name, *args, **kwargs):
#     print(name, args, kwargs)
# func5('world', 1,2,3, a=1, b
