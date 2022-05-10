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

