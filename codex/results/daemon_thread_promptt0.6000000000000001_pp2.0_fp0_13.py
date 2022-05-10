import threading
# Test threading daemon

def hello():
    print 'hello, world'
    
t = threading.Timer(5.0, hello)
t.daemon = True
t.start()

while True:
    pass


from multiprocessing import Process
from multiprocessing import Value

def f(n):
    n.value = 3.1415927

if __name__ == '__main__':
    num = Value('d', 0.0)
    p = Process(target=f, args=(num,))
    p.start()
    p.join()

    print num.value

from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f,
