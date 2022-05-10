import sys, threading

def run():
    print "current thread's name: %s" % threading.current_thread().name

    t1 = threading.Thread(target=run_thread, name="t1", args=(1,))
    t2 = threading.Thread(target=run_thread, name="t2", args=(2,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print "main thread exits."

def run_thread(arg):
    print "current thread's name: %s, arg: %s" % (threading.current_thread().name, arg)

run()
