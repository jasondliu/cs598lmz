import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test time.sleep()
start = time.time()
for _ in range(5):
    time.sleep(0.1)
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test time.perf_counter()
start = time.perf_counter()
for _ in range(5):
    time.sleep(0.1)
end = time.perf_counter()
print('Took %.3f seconds' % (end - start))

# Test time.process_time()
start = time.process_time()
for _ in range(5):
    time.sleep(0.1)
end = time.process_time()
print('Took %.3f seconds' % (end -
