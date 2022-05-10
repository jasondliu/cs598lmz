import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()
sys.stdin.readline()

# 4.
# -*- coding: utf-8 -*-
import time
for i in range (10):
    print(i)
    time.sleep(1)

# 5.
import time
for i in range(10):
    print(i)
    time.sleep(2)
else:
    print('The for loop is over')

# 6.
# -*- coding: utf-8 -*-
import time
for i in range(2):
    print(i)
    time.sleep(1)
    break
    print('Здесь будет выводиться четные числа')

# 7.
import time
for i in range(2):
    print(i)
    time.sleep(1)
    continue
    print('Здесь будет выводитьс
