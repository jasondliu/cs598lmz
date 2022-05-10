import sys, threading

def run():
    while True:
        print(threading.current_thread().name)

if __name__ == '__main__':
    for i in range(100):
        t = threading.Thread(target=run)
        t.start()
