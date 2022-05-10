import threading
# Test threading daemon
import time
import requests
import json

class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting " + self.name)
        get_request(self.name)
        print("Exiting " + self.name)


def get_request(thread_name):
    url = "https://www.alphavantage.co/query"
    payload = {'function': 'TIME_SERIES_DAILY',
               'symbol': 'MSFT',
               'apikey': 'demo'}
    response = requests.get(url, params=payload)
    data = json.loads(response.text)
    print(data)

thread1 = MyThread(1, "Thread-1")
thread2 = MyThread(2, "Thread-2")

thread1.start()
thread2.start()

print("Exiting Main Thread")
