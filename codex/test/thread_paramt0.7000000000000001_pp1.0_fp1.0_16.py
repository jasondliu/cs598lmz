import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()
"""
"""
import threading, time

def counter(myId, count):                          # Функция потока
    for i in range(count):
        time.sleep(1)                              # Задержка в одну секунду
        print('[%s] => %s' % (myId, i))

for i in range(5):                                 # Создать пять потоков
    threading.Thread(target=counter, args=(i, 5)).start()
print('Main thread exiting.')

"""
"""
import threading, time

