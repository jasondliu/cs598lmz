import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, itertools.product(*map(int, sys.stdin.read().split('\n'))))))).start()

# Задача 4. Поиск самого длинного префикса
import sys
a, b = next(sys.stdin), next(sys.stdin)
i = len(a)
while i != 0 and a[:i] != b[:i]:
  i -= 1
print(a[:i])

# Задача 5. Деление на пары
import sys, itertools
a = next(sys.stdin)
b = sys.stdin.readlines()
print(' '.join(map(lambda x: '%d %d' % (x[0], x[1]), sorted(itertools.combinations(sorted(map(int, b)), 2)))))

#
