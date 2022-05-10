import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

from multiprocessing import Process, Queue
import time, numpy as np, cv2

N = 5

def recv_msg(queue):
    while True:
        msg = queue.get()
        if msg == 'kill':
            break

def main():
    queue = Queue()

    recv_p = Process(target=recv_msg, args=(queue,))
    recv_p.start()

    for i in range(N):
        queue.put(i)
        time.sleep(1)

    queue.put('kill')
    recv_p.join()

if __name__ == '__main__':
    main()
