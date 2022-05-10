import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()
sleep(10)

# sys.stdout.write('\a')
