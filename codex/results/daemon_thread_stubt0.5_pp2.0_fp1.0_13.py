import sys, threading

def run():
    while True:
        print 'thread'
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.setDaemon(True)  # 守护线程
    t.start()
    while True:
        print 'main'
        time.sleep(1)
        if raw_input() == 'q':  # 在父线程的输入中输入q时结束程序，即使子线程在运行
            sys.exit()
