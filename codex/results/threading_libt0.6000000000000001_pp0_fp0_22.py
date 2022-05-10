import threading
threading.Thread(target=lambda: None).start()

# RuntimeError: Cannot start new thread

def f():
    print('f()')
    return

threading.Thread(target=f).start()

# f()
