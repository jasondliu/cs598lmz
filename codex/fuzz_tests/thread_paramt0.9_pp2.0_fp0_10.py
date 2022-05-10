import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

# DO NOT USE:
#import thread
#thread.start_new(lambda: sys.stdout.write('.'), ())

time.sleep(5)
sys.exit()
