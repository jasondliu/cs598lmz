import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input('INPUT > '))).start()

import requests
for i in range(300):
	requests.get('http://localhost:5000/')
