import select
# Test select.select([], [], [], 5) on an empty array.
select.select([], [], [], 5)
# Test select.poll() on an empty poll set
p = select.poll()
p.poll()
p.poll(5)
```

### multiprocessing

```py
from multiprocessing import Pool

def f(x):
    return x*x


pool = Pool(processes=4)              # start 4 worker processes
result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
print(result.get(timeout=1))           # prints "100" unless your computer is *very* slow

print(pool.map(f, range(10)))         # prints "[0, 1, 4,..., 81]"

it = pool.imap(f, range(10))
print(next(it))                       # prints "0"
print(next(it))                       # prints "1"
print(it.next(timeout=1))             # prints "4" unless your computer is *very* slow


