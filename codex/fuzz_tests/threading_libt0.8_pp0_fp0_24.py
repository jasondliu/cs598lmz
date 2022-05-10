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
</code>
the Auth is just a simple scheduler to do a long-polling type of request, and the authSock is just a socket that I use to send the request, it doesn't actually do any of the work; 
<code>self.authSock.recv(1024)</code> just recieves the response and then passes a variable to the main thread to tell it to do something.
Once I close the window, the app will go into it's maintainConnection loop and try to connect, but it never seems to actually connect.  I'm not sure what I'm doing wrong, but I would appreciate any help.


A:

You need to make sure that the thread
