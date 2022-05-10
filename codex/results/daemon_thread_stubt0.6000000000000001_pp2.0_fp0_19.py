import sys, threading

def run():
    while True:
        if not q.empty():
            item = q.get()
            if item is None:
                break
            print('do ' + str(item))
        time.sleep(.1)

q = queue.Queue()
threading.Thread(target=run).start()

for i in range(100):
    q.put(i)

q.put(None)
</code>

