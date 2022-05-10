import threading
threading.current_thread().name

t = threading.Thread(target=count, args=(1,5))
t.start()
print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread().name)

t = threading.Thread(target=count, name='Thread-1', args=(1,5))
t.start()
print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread().name)

t = threading.Thread(target=count, name='Thread-1', args=(1,5))
t.start()
t.join() #等待线程结束后再继续主线程
print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread().name)

def count(start, end):
    while start <= end:
        time.sleep(1)
