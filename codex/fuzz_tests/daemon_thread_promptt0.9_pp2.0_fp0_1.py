import threading
# Test threading daemon feature
class Timer(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            time.sleep(1)
            print("tik")
        print("bye")

    def cancel(self):
        self.event.set()

a_timer = Timer()
a_timer.start()
time.sleep(10)
a_timer.cancel()
time.sleep(5)
```


## Functional programming

### lambda functions (one-liner functions)

```python
foo = lambda x,y,z: x+2*y+3*z
>>> foo(1,2,3)
# 12
```

### map()

`map()` is a higher order function that applies a given function to each item of an iterable and returns a list of the results.
- The first argument function is applied to each item of iterable, yielding the results.
- The map()
