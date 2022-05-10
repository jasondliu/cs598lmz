import sys, threading
threading.Thread(target=lambda: sys.stderr.write('brrrrrr\n'), start=False).start()
 
print('main thread writes')
 
### OUTPUT ###
# main thread writes
# brrrrrr
