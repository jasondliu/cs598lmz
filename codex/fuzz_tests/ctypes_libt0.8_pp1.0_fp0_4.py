import ctypes
ctypes.util.find_library("gmp")

#import module
import fibonacci

#Run fib(n)
fibonacci.fib(10)
```

```
$ python3 run.py
```

```
> 55
```
