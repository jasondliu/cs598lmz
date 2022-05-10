import sys, threading

def run():
    for i in range(10):
        print('thread running')
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('thread end')
