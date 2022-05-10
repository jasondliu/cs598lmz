import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test threading.Thread

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)

threads = []
for i in range(5):
    thread = threading.Thread(target=compute_helicopter_location, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Test threading.Thread with queue

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value =
