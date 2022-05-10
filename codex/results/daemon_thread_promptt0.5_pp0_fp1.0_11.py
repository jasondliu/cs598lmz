import threading
# Test threading daemon

def f():
    print('hello')
    threading.Timer(5.0, f).start()

f()
