import sys, threading

def run():
    print('process (%s) start ...' % os.getpid())
    pid = os.fork()   # 子进程也要执行fork()方法，父进程也会返回子进程的pid，而子进程会返回0，表示成功创建
    if pid > 0 :
        # 父进程执行
        print('parent process (%s) and child is %s.' % (os.getpid(), pid))
        sys.exit(0)
    else:
        # 子进程执行
        os.setsid()
        print('child process (%s) start ...' % os.getpid())


def linux_daemonize():
    run()
    
    # 创建守护进程的最后一步，让
