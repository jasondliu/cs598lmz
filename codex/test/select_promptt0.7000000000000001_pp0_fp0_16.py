import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))


from threading import Thread

def compute_helicopter_location(index):
    pass

for i in range(5):
    Thread(target=compute_helicopter_location, args=(i,)).start()


import queue
q = queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print('Process %s' % q.get())

q = queue.Queue()
def consumer():
    print('Consumer waiting')
    q.get()                  # Runs after put() below
    print('Consumer done')

thread = Thread(target=consumer)
thread.start()

def producer():
    print('Producer putting')
    q.put(object())         # Runs before get() above
