import sys, threading

def run():
    print('Thread %s is running...' % threading.current_thread().name)

def main():
    print('Thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run, name='MyThread')
    t.setDaemon(True)
    t.start()
    sys.exit()

if __name__ == '__main__':
    main()

# 程序的输出结果
# Thread MainThread is running...
# Thread MyThread is running...
# Process finished with exit code 0

# 说明
# 1. 主线程调用setDaemon()，设置守护线程为主线程；
# 2. 主线程调用sys.exit()，退出脚本，主线程
