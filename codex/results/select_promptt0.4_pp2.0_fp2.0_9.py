import select
# Test select.select()

def slow_systemcall():
    select.select([],[],[],0.1)

start=time.time()
for i in range(5):
    slow_systemcall()
end=time.time()
print(end-start)

start=time.time()
for i in range(5):
    time.sleep(0.1)
end=time.time()
print(end-start)

# select.select() is faster than time.sleep()

# Test select.poll()

start=time.time()
for i in range(5):
    select.select([],[],[],0.1)
end=time.time()
print(end-start)

start=time.time()
p=select.poll()
for i in range(5):
    p.poll(0.1)
end=time.time()
print(end-start)

# select.poll() is faster than select.select()

# Test select.epoll()

start=time.time()
for i in range(5):
    select.select
