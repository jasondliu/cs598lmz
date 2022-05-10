import threading
# Test threading daemon to see if it works
import time

class DaemonThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name, daemon=True)

    def run(self):
        while True:
            time.sleep(1)
        print("Should never see this!")

thread = DaemonThread('daemon thread')
thread.start()

# Why use objects

# Why inherit

# Why use properties

# Why use closure
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3))
print(add_10(100))

set_x = create_adder(x)


# Why use *args
def multiple_args(a, b, *args):
    return a + b + sum(args)


# Why use **kwargs
def multiple_kwargs(a, b, *args, **kwargs):
    return a + b + sum(args) + sum
