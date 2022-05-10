import threading
# Test threading daemon with a 5 second timer
def hello():
    print('hello')
    threading.Timer(5.0, hello).start()

hello()

# Test threading daemon with a 5 second timer
def goodbye():
    print('goodbye')
    threading.Timer(5.0, goodbye).start()

goodbye()
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python3 threading_daemon.py
hello
goodbye
```

```bash
$ python
