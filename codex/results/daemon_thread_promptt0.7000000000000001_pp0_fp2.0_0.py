import threading
# Test threading daemon
def do_something(seconds):
    print(f' Sleep for {seconds} seconds(s)')
    time.sleep(seconds)
    print(' Done sleeping')

start = time.perf_counter()

t1 = threading.Thread(target=do_something, args=[1.5])
t2 = threading.Thread(target=do_something, args=[1.5])

t1.start()
t2.start()

t1.join()
t2.join()
finish = time.perf_counter()

print(f' Finished in {round(finish-start, 2)} second(s)')

# A non-daemon thread will keep the application running until it has finished executing.
# A daemon thread will be killed once all the non-daemon threads have been killed.
# The main thread is a non-daemon thread.
