import threading
# Test threading daemon
def f():
    while True:
        print("Hello world")
        time.sleep(1)

t1 = threading.Thread(target=f)
t1.daemon = True
t1.start()

#t1.join()

#t2 = threading.Thread(target=f)
#t2.daemon = True
#t2.start()


print("\n\n")
print("Test threading daemon")
print("\n\n")

# Test threading with lock
def g(l,i):
    l.acquire()
    print("Hello world",i)
    time.sleep(1)
    l.release()

lock = threading.Lock()

for i in range(10):
    t = threading.Thread(target=g, args=(lock,i))
    t.start()

print("\n\n")
print("Test threading with lock")
print("\n\n")


# Test threading with lock 2
def h(l,i):
    l.acquire()

