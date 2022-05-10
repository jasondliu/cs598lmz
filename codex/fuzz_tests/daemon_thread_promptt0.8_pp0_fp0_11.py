import threading
# Test threading daemon to send the data
class TestThread(threading.Thread):
    def __init__(self, test_queue, url_update):
        threading.Thread.__init__(self)
        self.url_update = url_update
        self.test_queue = test_queue
        self.daemon = True
        self.start()

    def run(self):
        while True:
            if self.test_queue:
                try:
                    data = self.test_queue.pop(0)
                    resp = requests.post(self.url_update, data=json.dumps(data))
                    print "sent data: " + json.dumps(data) + " - " + str(resp.status_code)
                except IndexError:
                    pass

# Test threading daemon to send the data
class TestThread2(threading.Thread):
    def __init__(self, test_queue, url_update):
        threading.Thread.__init__(self)
        self.url_update = url_update
        self.test_queue = test_queue
       
