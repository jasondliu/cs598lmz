import sys, threading

def run():
    while True:
        print('thread {} running'.format(threading.current_thread().name))
        time.sleep(1)


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=run)
        threads.append(t)

    for t in threads:
        t.start()
        t.join()
