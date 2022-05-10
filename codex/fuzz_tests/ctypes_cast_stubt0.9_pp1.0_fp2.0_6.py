import ctypes
ctypes.cast(0, ctypes.py_object).value

def thread_function(name):
    print("Thread %s: starting" % name)
    time.sleep(0.5)
    print("Thread %s: finishing" % name)

x = threading.Thread(target=thread_function, args=("1",))
y = threading.Thread(target=thread_function, args=("2",))

x.start()
y.start()


def slow_systemcall():
	select.select([],[],[],0.1)
	
start = time.time()
for _ in range(5):
	slow_systemcall()
end = time.time()
print(end - start)


# deque('abc') has the same effect as list("abc").
# del d[0] is an efficient way to remove an element from the left side of a deque.
# list.popleft() and collections.deque.popleft() are identical ways to pop an item from the left side of a list or deque.
# list.append() and collections.deque.
