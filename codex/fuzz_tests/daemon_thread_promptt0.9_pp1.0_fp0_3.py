import threading
# Test threading daemon below
#print("Start of Program")
#def take_nap():
#    time.sleep(5)
#    print("wake up!")
#threadObj = threading.Thread(target=take_nap)
#threadObj.start()
#
#print("End of Program")

# thread class to take photo every so often while in car
class Photos(threading.Thread):
    def __init__(self, interval=1):
        threading.Thread.__init__(self)
        self.interval = interval
        self.next_call = time.time()

    # function that takes photo based on class interval 
    def run(self):
        while True:
            self.next_call = self.next_call + self.interval
            t = threading.Timer(self.next_call - time.time(), self.run)
            t.start()
            # code to be run by thread goes here
            # i.e. take picture
            newtime = datetime.datetime.now().strftime("%Y-%m-%d %H_
