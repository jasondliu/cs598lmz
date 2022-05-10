from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x:x for x in [1]}
e = {x for x in range(1000000)}
f = set(range(1000000))

def timeit(func): 
    def wrapper(*args, **kwargs): 
        start = time.time() 
        result = func(*args, **kwargs) 
        end =time.time() 
        print(func.__name__, end-start) 
        return result 
    return wrapper 

def test(obj):
    if isinstance(obj, (set, dict)):
        for _ in obj:
            pass
    else:
        for _ in obj:
            pass

g = timeit(test)
g(a)
g(b)
g(c)
g(d)
g(e)
g(f)

# test 0.0
# test 0.0
# test 0.0
# test 0.0
# test 0.0
# test 0.
