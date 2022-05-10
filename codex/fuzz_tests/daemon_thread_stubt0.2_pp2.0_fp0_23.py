import sys, threading

def run():
    sys.stdout.write('Hello from child, pid %s\n' % os.getpid())
    sys.exit(0)

def test():
    sys.stdout.write('Hello from parent, pid %s\n' % os.getpid())
    childpid = os.fork()
    if childpid == 0:
        run()
    else:
        sys.stdout.write('Hello from parent, pid %s, child is %s\n' % (os.getpid(), childpid))
    sys.exit(0)

if __name__ == '__main__':
    test()
