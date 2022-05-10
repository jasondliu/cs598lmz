import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()
print('main')
# main
# thread
#
print('thread' in dir(threading.Thread)) # True
