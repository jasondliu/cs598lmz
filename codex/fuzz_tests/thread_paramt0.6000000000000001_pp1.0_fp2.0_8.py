import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
```

```bash
$ echo "hello" | python3 main.py
hello
```
