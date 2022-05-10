import sys, threading

def run():
    for i in range(1, 30):
        print(threading.current_thread().name, ' : ', i)
        time.sleep(1)

if __name__ == '__main__':
    print('Start')
    threads = []
    for i in range(3):
        t = threading.Thread(name='A' + str(i), target=run)
        t.setDaemon(True)
        t.start()
        threads.append(t)
    for T in threads:
        T.join()
    print('End')
