import sys, threading
threading.Thread(target=lambda: sys.stdout.write('foobar\n')).start()

print 'main thread continuing'

# (end)
