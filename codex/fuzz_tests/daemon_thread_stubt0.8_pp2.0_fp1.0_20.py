import sys, threading

def run():
    while True:
        if not q.empty():
            item = q.get()
            if item is None:
                break
            print('...', item)
            time.sleep(0.5)

if __name__ == '__main__':
    Njobs = 10
    q = queue.Queue()

    thread = threading.Thread(target=run)
    thread.start()
    for i in range(Njobs):
        q.put(i)
    q.put(None)
    thread.join()
