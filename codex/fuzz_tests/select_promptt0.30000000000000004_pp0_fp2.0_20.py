import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print(end - start)

# Test time.sleep()
start = time.time()
for i in range(5):
    time.sleep(0.1)
end = time.time()
print(end - start)

# Test time.clock()
start = time.clock()
for i in range(5):
    slow_systemcall()
end = time.clock()
print(end - start)

# Test time.perf_counter()
start = time.perf_counter()
for i in range(5):
    slow_systemcall()
end = time.perf_counter()
print(end - start)

# Test time.process_time()
start = time.process_time()
for i in range(5):
    slow_systemcall()
end = time.process_time()
print(end - start)
