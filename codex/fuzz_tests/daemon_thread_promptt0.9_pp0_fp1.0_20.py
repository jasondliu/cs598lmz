import threading
# Test threading daemon
print(event.is_set())
event.set()
print(event.is_set())
event.clear()
print(event.is_set())

# Test threading 
t = threading.Thread(name='main')
t.start()
print(t.is_alive())
t.join()
print(t.is_alive())


# Test pass
def foo(x=None):
    if x != None:
        print(len(x))
    else:
        print('x is None')
        
foo([1,2,3])
foo()

a = [1,2,3]
foo(a)

# Test try catch
try:
    raise KeyError('key1')
except KeyError as e:
    print(e)

import math
# Test float
a = 1.1 + float('2.2')
print(a)
b = float('inf') + 1
print(b)
print(math.isinf(b))

# Test math
num = 0
while (num < 1000):
    num
