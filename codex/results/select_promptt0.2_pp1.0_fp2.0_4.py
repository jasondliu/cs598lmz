import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test threads

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

# Test threads

import threading

class ComputeHelicopterLocation(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        pass

threads = []
for i in range(5):
    thread = ComputeHelicopterLocation(i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Test threads

import threading

class ComputeHelicopterLocation(threading
