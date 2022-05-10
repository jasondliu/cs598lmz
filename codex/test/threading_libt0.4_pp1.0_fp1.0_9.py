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
