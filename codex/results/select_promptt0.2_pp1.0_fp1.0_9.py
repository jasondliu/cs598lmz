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

def compute_helicopter_location(index):
    pass

threads = []
for i in range(5):
    thread = threading.Thread(target=compute_helicopter_location, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Test threads

def compute_helicopter_location(index):
    pass

threads = []
for i in range(5):
    thread = threading.Thread(target=compute_helicopter_location,
