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

start = time.time()
threads = []
for i in range(5):
    thread = threading.Thread(target=compute_helicopter_location, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print('Took %.3f seconds' % (end - start))

# Test processes

def compute_helicopter_location(index):
    pass

start = time.time()
