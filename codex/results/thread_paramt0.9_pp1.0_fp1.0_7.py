import sys, threading
threading.Thread(target=lambda:sys.stdout.write('平手\n')).start()
import time
time.sleep(1)
sys.exit()
