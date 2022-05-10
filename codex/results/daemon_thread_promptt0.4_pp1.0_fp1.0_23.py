import threading
# Test threading daemonic

def worker():
    print("Worker")
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    threads.append(t)
    t.start()

print("End")

# Test threading daemonic

def worker():
    print("Worker")
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print("End")
 
# Test threading daemonic

def worker():
    print("Worker")
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print("End")
 
# Test threading daemonic

def worker():
    print("Worker")
    return

threads = []

for i in range(5):
   
