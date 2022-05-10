import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# we can also use a thread to run a function that takes arguments
def my_function(arg1, arg2):
    sys.stdout.write(f'Hello from thread 3 with {arg1} and {arg2}\n')
threading.Thread(target=my_function, args=['arg1', 'arg2']).start()

# we can also use a thread to run a class method
class MyClass(threading.Thread):
    def run(self):
        sys.stdout.write('Hello from thread 4\n')
MyClass().start()

# we can also use a thread to run a class method that takes arguments
class MyClass(threading.Thread):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        threading.Thread.__init__(self)
