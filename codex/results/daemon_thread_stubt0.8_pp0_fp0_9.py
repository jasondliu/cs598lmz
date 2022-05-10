import sys, threading

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(10)
    while True:
            client, address = server.accept()
            ct = client_thread(client)
            ct.start()

class client_thread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        size = 1024
        while True:
            try:
                data = self.client.recv(size)
                if data:
                    # set the response to echo back the recieved data
                    self.client.send(data)
                else:
                    raise error('Client disconnected')
            except:
                self.client.close()
                return False

if __name__ == "__main__":
    if(len(sys.argv) < 2) :
        print 'Usage : python tcp-server.py host'
        host = raw_input
