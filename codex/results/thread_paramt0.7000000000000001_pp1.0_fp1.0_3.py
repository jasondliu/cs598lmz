import sys, threading
threading.Thread(target=lambda: sys.stdout.write("B")).start()
threading.Thread(target=lambda: sys.stdout.write("C")).start()
print("A")
```

### Execute
```bash
$ python3.6 -c "import sys, threading; threading.Thread(target=lambda: sys.stdout.write('B')).start(); threading.Thread(target=lambda: sys.stdout.write('C')).start(); print('A')"
ABC
```

### Execute (with "time")
```bash
$ time python3.6 -c "import sys, threading; threading.Thread(target=lambda: sys.stdout.write('B')).start(); threading.Thread(target=lambda: sys.stdout.write('C')).start(); print('A')"
ABC

real    0m0.019s
user    0m0.005s
sys     0m0.006s
```

## 4. Thread (with `print`)

### Source
```python
import sys, threading

