import threading
threading._DummyThread._Thread__stop = lambda x: 42
 
class MyThread(threading.Thread):
  def __init__(self, callback, event):
    threading.Thread.__init__(self)
    self.callback = callback
    self.event = event
 
  def run(self):
    self.callback()
    self.event.set()

def wait_for_internet_connection():
    while True:
        try:
            response = urlopen('https://www.google.com',timeout=1)
            return
        except Exception as e:
            print(e)
            time.sleep(1)

# threadObj = MyThread(wait_for_internet_connection, threading.Event())
# threadObj.start()
# threadObj.join()

# print('Program continues to run in foreground.')

def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus =
