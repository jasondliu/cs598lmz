import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    for i in range(10):
        print('main', i)
        time.sleep(1)
