import threading
# Test threading daemon
import time
import requests
import json

# Test threading daemon
def worker():
    while True:
        print("I'm working")
        time.sleep(1)

def main():
    # Test threading daemon
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

    # Test threading daemon
    for x in range(10):
        print("Main:", x)
        time.sleep(1)

    # Test requests
    #url = 'http://127.0.0.1:5000/api/v1/users/'
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #r = requests.post(url, data=json.dumps({"username":"test", "password":"test"}), headers=headers)
    #print(r.text)

    # Test requests
    #url = 'http://127.0.0.1:5000/api/v1/users/'
    #headers = {'Content-type': 'application/
