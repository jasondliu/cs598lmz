import sys, threading

def run():
    global flag
    while True:
        print "threading is running........"
        time.sleep(0.01)
        if flag > 0 :
            print "flag is a number : " , flag
            break
threads = []
t1 = threading.Thread(target=run)
threads.append(t1)
t2 = threading.Thread(target=run)
threads.append(t2)
t3 = threading.Thread(target=run)
threads.append(t3)

if __name__ == '__main__':
        flag = 1
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
