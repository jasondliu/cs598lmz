import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print(end - start)

# Coroutine Decorator

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

# Coroutine Example

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

coro_avg = averager()
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))

# Generator-Based Coroutine

from collections import namedtuple

Result = namedtuple('Result', 'count average')
