import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread 2\n')).start()
print 'Hello from\nMain thread'

# ----------------------------------------------------------------------------------------------------

def f(id):
    print 'function f called by thread', id

threads = []
for i in range(5):
    t = threading.Thread(target=f, args=(i,))
    threads.append(t)
    t.start()

# ----------------------------------------------------------------------------------------------------

def f(id):
    print 'function f called by thread', id

threads = []
for i in range(5):
    t = threading.Thread(target=f, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# ----------------------------------------------------------------------------------------------------

def f(id):
    print 'function f called by thread', id

threads = []
for i in range(5):
    t = threading
