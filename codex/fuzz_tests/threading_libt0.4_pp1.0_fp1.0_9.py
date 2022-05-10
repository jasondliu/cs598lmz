import threading
threading.stack_size(67108864)

import time

def func(n):
    print(n)
    time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=func, args=(5,))
    t.start()
    t.join()
</code>
В консоли выводится <code>5</code> и программа завершается.
При этом, если поменять <code>args=(5,)</code> на <code>args=(5,6)</code>, то в консоли появляется <code>5</code>, программа не завершается, а после сек
