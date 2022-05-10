import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(0.5)

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)

t1.start()
t2.start()

t1.join()
t2.join()

print('done')
