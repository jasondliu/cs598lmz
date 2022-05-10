import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 2
import sys
threading.Thread(target=lambda: sys.stdout.write(raw_input())).start()
```

## How to run

```
$ python3.6 main.py
```

## How to test

```
$ python3.6 -m unittest discover
```
