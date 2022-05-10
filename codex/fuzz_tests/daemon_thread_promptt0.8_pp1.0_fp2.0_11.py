import threading
# Test threading daemon
endTime = time.time() + 60 * 2
def countdown(n):
    while time.time() < endTime:
        print 'T-minus', n
        n -= 1
        time.sleep(5)
t = threading.Thread(target=countdown, args=(10,))
t.setDaemon(True)
t.start()
t.join()

# Test context manager
with open('/tmp/abc.txt', 'wt') as f:
    f.write('hello')

# Test list comprehension
#print [x**2 for x in range(10)]
#print [x**2 for x in range(10) if x % 3 == 0]
#print [(x, y) for x in range(10) if x % 2 == 0 
#            for y in range(10) if y % 2 == 1]

# Test dict comprehension
#print {x: x**2 for x in range(10)}
#print {x: 'A' + str(x) for x in range(10)}

# Test generator
#g = (x**2 for
