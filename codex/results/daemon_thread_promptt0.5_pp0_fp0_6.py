import threading
# Test threading daemon

def hello():
    while True:
        print("hello")
        time.sleep(1)

t = threading.Thread(target=hello, args=())
t.setDaemon(True)
t.start()

print("Main thread")

time.sleep(10)
print("Main thread end")

# Main thread
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# Main thread end

# Process

import multiprocessing
# Test multiprocessing daemon

def hello():
    while True:
        print("hello")
        time.sleep(1)

p = multiprocessing.Process(target=hello, args=())
p.daemon = True
p.start()

print("Main process")

time.sleep(10)
print("Main process end")

# Main process
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# Main process end

# Main process
