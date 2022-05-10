import sys, threading

def run():
    while 1:
        print threading.currentThread().getName(), 'Outputting...'

threads = []
for i in range(5):
    t = threading.Thread(target=run)
    threads.append(t)
    t.start()

if __name__ == '__main__':
    for i in threads:
        i.join()
