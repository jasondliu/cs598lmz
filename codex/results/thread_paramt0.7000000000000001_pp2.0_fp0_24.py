import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()

print("Hello from main thread")

## Hello from main thread
## Hello from thread 2
```

## Threadpool

> Thread pool is a way of managing a pool of worker threads and then dispatching tasks to those worker threads.

```python
import concurrent.futures

def func_1(arg):
    print(f"func_1({arg})")

def func_2(arg):
    print(f"func_2({arg})")

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit work to the executor
        future_1 = executor.submit(func_1, 1)
        future_2 = executor.submit(func_2, 2)

        # Wait until both tasks are completed
        future_1.result()
        future_2.result()

main()

## func_1(1)
## func_2(2)
```

We can also use
