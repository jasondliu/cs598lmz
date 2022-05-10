import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    print('main thread')
    time.sleep(3)
    print('done')

