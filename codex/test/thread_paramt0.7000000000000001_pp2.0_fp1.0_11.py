import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world!\n')).start()
 
# vim: et sw=4 sts=4
