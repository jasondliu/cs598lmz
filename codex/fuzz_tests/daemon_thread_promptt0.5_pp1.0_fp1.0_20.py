import threading
# Test threading daemon

def my_function():
    print("\nStarted")
    time.sleep(5)
    print("\nEnded")

my_thread = threading.Thread(target=my_function)
my_thread.setDaemon(True)
my_thread.start()

print("\nProgram ended")

# Test threading without daemon

def my_function():
    print("\nStarted")
    time.sleep(5)
    print("\nEnded")

my_thread = threading.Thread(target=my_function)
my_thread.start()

print("\nProgram ended")

# Test threading without daemon

def my_function():
    print("\nStarted")
    time.sleep(5)
    print("\nEnded")

my_thread = threading.Thread(target=my_function)
my_thread.start()

print("\nProgram ended")

# Test threading without daemon

def my_function():
    print("\nStarted")
    time.sleep(5
