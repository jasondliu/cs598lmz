import sys, threading

def run():
    print('Hello from thread {}'.format(threading.get_ident()))

sys.exit(run())
