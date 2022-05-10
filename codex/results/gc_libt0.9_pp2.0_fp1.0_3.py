import gc, weakref, os

def profiler(frame, event, arg):
    if event == 'call':
        stack.append(frame.f_code.co_name)
    elif event == 'return':
        stack.pop()
    return profiler

def test(func):
    sys.setprofile(profiler)
    try:
        func()
    finally:
        sys.setprofile(None)
    
def func():
    a = range(100)

test(func)
</code>
output:
<code>In [49]: test(func)
In [50]: stack
Out[50]: ['range']
In [51]: 
</code>
Edit:
You could also use cProfile to get the needed info.
<code>import cProfile

def test(func):
    cProfile.runctx('func()', {'func': func}, {})

def func():
    a = range(100)

test(func)
</code>
output:
<code>In [59]: test(func)
In [60]: 
         427
