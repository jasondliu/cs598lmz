import threading
# Test threading daemon

def foo():
    print('Hello world')
    time.sleep(0.1)

t = threading.Thread(target=foo)
t.daemon = True
t.start()
t.join()

print('Exiting')

# Test Queue class
q = queue.Queue()
q.put(1)
q.put(2)
print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())

# Test Set
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.add(1)
print(s)
s.add(3)
print(s)
s.remove(3)
print(s)
s.remove(3)
print(s)

# Test ordered dictionary
d = collections.OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d['eggs'] = 5

for key
