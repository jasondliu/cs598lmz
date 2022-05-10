import sys, threading

def run():
    time.sleep(3)
    threading.Thread(target=test_wsgiserver).start()


if __name__ == '__main__':
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
    threading.Thread(target=run).start()
