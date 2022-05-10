import sys, threading
threading.Thread(target=lambda: sys.stderr.write("hello world\n")).start()
```

```
$ python3 -u test.py
```

```
hello world
```

```
$ python2 -u test.py
```

```
hello world
```

```
$ node test.js
```

```
hello world
```

```
$ ./test
```

```
hello world
```

```
$ ./test.py
```

```
hello world
```

```
$ ./test.py2
```

```
hello world
```

```
$ ./test.js
```

```
hello world
```

```
$ ./test.js2
```

```
hello world
```

```
$ ./test.js3
```

```
hello world
```

```
$ ./test.js4
```

```
hello world

