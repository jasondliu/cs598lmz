import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\x1b]2;{0}\x07".format("tst"))).start()
threading.Thread(target=lambda:sys.stdout.write("\x1b]2;{0}\x07".format("tst2"))).start()

stdout_locks = set() # protects (does not lock) printing to STDOUT
lock_stdout = False # lock STDOUT when True
isatty = sys.stdout.isatty()

def mt_print(msg):
    stdout_locks.add(threading.get_ident())
    if lock_stdout and isatty:
        sys.stdout.write("\x1b[?25h")

    sys.stdout.write("\n Thread Id: "+str(threading.get_ident())+" | ")
    sys.stdout.write(msg)

    if lock_stdout and isatty:
        sys.stdout.write("\x1b[?25l")
    stdout_locks.discard(threading.get_ident
