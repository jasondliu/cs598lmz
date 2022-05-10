import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()

def do_nothing():
    pass

timer = threading.Timer(1.0, do_nothing)
timer.start()
print('main')
timer.join()
print('after')
