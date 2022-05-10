import threading
# Test threading daemon
a = threading.Thread(target=time.sleep, args=(1,))
print(a.daemon)
a.daemon = True
print(a.daemon)



import threading

def test(x):
    print(x)
    print(threading.current_thread().name)

a = threading.Thread(target=test, args=(42,))
a.start()
a.join()
