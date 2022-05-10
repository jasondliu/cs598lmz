import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test threading.Thread

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

# Test threading.Thread

from threading import Thread

class ComputeHelicopterLocationThread(Thread):
    def __init__(self, index):
        super().__init__()
        self.index = index
    def run(self):
        compute_helicopter_location(self.index)

threads = []
for i in range(5):
    thread = ComputeHelicopterLocationThread(i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Test threading.Thread

