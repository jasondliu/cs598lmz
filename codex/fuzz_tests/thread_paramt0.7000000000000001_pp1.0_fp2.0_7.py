import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'*int(input()))).start()
```

### [C. Враги](https://codeforces.com/contest/1186/problem/C)
```python
n = int(input())
l = list(map(int, input().split()))
l = list(sorted(l))
print('0')
for i in range(n-1):
    if l[i] == l[i+1]:
        print('0')
    else:
        print(l[i+1]-l[i])
print('0')
```

### [D. Комната для двоих](https://codeforces.com/contest/1186/problem/D)
```python
from math import ceil

n = int(input())
l = list(map(int, input().split()))

l = list(sorted(l))

ind = 0

for i in range(len(l)
