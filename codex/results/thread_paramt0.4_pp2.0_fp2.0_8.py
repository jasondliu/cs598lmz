import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# python3 -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()'
```

```
$ python3 -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()' < /etc/passwd
```

## 実行例

```
$ python3 -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()' < /etc/passwd > /tmp/passwd
$ diff /tmp/passwd /etc/passwd
```
