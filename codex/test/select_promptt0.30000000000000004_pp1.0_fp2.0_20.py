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

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

database = FakeDatabase()

print(f'Testing update. Starting value is {database.value}')

threads = [threading.Thread(target=database.update, args=(i,)) for i in range(5)]

for thread in threads: thread.start()
