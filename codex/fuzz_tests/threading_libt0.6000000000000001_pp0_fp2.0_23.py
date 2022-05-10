import threading
threading.Thread(target=start_server).start()

import time
time.sleep(2)

import requests

ret = requests.get('http://127.0.0.1:5000/')
print(ret)
