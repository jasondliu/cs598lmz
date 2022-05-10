import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from the other thread\n")).start()

#9.3
def do_something(x):
    print("Doing something with", x)

def do_something_else(x):
    print("Doing something else with", x)

def do_something_and_something_else(x):
    do_something(x)
    do_something_else(x)

def do_something(x):
    print("Doing something with", x)

def do_something_else(x):
    print("Doing something else with", x)

def do_something_and_something_else(x):
    threading.Thread(target=do_something, args=(x,)).start()
    threading.Thread(target=do_something_else, args=(x,)).start()

def do_something(x):
    print("Doing something with", x)

def do_something_else(x):
    print("Doing something else with", x)

