import select
# Test select.select()

def slow_systemcall():
    select.select([],[],[],0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end-start))

# Output
# Took 0.501 seconds

def slow_systemcall():
    select.select([],[],[],0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end-start))

# Output
# Took 0.502 seconds

def slow_systemcall():
    select.select([],[],[],0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end-start))

# Output
# Took 0.501 seconds

from gevent import monkey; monkey.patch_all()
