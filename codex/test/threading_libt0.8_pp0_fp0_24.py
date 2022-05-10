import threading
threading.Thread(target = self.maintainConnection).start()

def maintainConnection(self):
    while(True):
        if(self.connectSock.getpeername()[0] == ""):
            print("Connecting...")
            self.connectSock.connect((self.servername, self.port))
            self.scheduleAuth()
            time.sleep(15)
        else:
            time.sleep(5)
