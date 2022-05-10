import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Test timeit.timeit()

print(timeit.timeit('math.sqrt(2)', 'import math', number=1000000))

# Test timeit.repeat()

print(timeit.repeat('math.sqrt(2)', 'import math', number=1000000))

# Test timeit.Timer()

t = timeit.Timer('math.sqrt(2)', 'import math')
print(t.timeit(number=1000000))
print(t.repeat(number=1000000, repeat=3))
