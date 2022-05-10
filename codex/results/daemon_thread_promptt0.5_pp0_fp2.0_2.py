import threading
# Test threading daemon

def foo():
    print("Hello, world!")
    time.sleep(1)

for i in range(10):
    t = threading.Thread(target=foo)
    t.setDaemon(True)
    t.start()

print("Main thread finishes")

# Main thread finishes
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!

# Main thread finishes
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!

# Main thread finishes
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
# Hello, world!
#
