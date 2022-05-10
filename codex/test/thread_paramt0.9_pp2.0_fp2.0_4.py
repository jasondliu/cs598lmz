import sys, threading
threading.Thread(target=lambda: sys.stdout.write('test\n')).start()
# need to call print to ensure we flush the stdout buffer
print
