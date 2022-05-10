import threading
threading.Thread(target=lambda: None).start()
import time
time.sleep(1)
import os
os.system("python3.7 server.py")
