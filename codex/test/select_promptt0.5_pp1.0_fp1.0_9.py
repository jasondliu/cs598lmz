import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

from threading import Thread

def compute_helicopter_location(index):
    pass

for i in range(5):
    Thread(target=compute_helicopter_location, args=(i,)).start()

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

database = FakeDatabase()
print('Starting value is %d' % database.value)

t1 = Thread(target=database.update, args=('Alice',))
t2 = Thread(target=database.update, args=('Bob',))
