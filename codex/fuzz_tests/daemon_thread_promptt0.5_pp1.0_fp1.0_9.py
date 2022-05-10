import threading
# Test threading daemon mode

# t = threading.Thread(target=lambda: print('hello'), daemon=True)
# t.start()
# print('main thread')

# Test threading join

# t = threading.Thread(target=lambda: print('hello'))
# t.start()
# t.join()
# print('main thread')

# Test threading lock

lock = threading.Lock()

def f():
    with lock:
        print('hello')

t = threading.Thread(target=f)
t.start()
t.join()
print('main thread')

# Test threading pool

# def f(x):
#     return x*x

# pool = ThreadPool(processes=4)
# result = pool.apply_async(f, (10,))
# print(result.get(timeout=1))

# Test threading pool with lock

# def f(x, lock):
#     with lock:
#         return x*x

# lock = threading.Lock()
# pool = ThreadPool(process
