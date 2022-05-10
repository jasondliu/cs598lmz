import threading
# Test threading daemon
import multiprocessing
import time

# Thread to run the server
class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        print "Starting server"
        app.run(host='0.0.0.0')
        print "Server running"

# Thread to run the client
class ClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        print "Starting client"
        time.sleep(5)
        #self.client = Client()
        print "Client running"

#threads = []
#threads.append(ServerThread())
#threads.append(ClientThread())

#for thread in threads:
#    thread.start()

#for thread in threads:
#    thread.join()

#print "Done"

if __name__ == '__main__':
