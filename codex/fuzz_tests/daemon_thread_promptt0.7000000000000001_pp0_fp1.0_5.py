import threading
# Test threading daemon

def test_func():
    print("Hello World")

t = threading.Thread(target=test_func)
t.daemon = True
t.start()

# However, the "Hello World" won't be printed out in the terminal

# The reason is because the program will terminate before the thread can start.

# A simple solution is to add a sleep timer.

# import time
# time.sleep(1)
