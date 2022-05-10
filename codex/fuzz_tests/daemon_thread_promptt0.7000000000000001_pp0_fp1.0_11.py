import threading
# Test threading daemon

def test(x):
    for i in range(x):
        print(i, end='')

t = threading.Thread(target=test, args=(100,))
t.setDaemon(True)
t.start()
print(threading.active_count())

# Test multiprocessing
from multiprocessing import Process

def test2(x):
    print(x)

p = Process(target=test2, args=(100,))
p.start()

# Test multiprocessing manager
from multiprocessing import Manager

m = Manager()
d = m.dict()
d['a'] = 1
d['b'] = 2
print(d)

l = m.list()
l.append(1)
l.append(2)
print(l)
