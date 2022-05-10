import sys, threading

def run():
    for i in range(2):
        print(threading.currentThread().getName() + ' ' + str(i))

if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=run, name='Thread-'+str(i))
        t1.start()
