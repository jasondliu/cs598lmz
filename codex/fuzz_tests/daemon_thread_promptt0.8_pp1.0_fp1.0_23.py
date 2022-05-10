import threading
# Test threading daemon
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')
        return

for i in range(500):
    logging.debug('i')
    t = MyThread()
    t.setDaemon(True)
    t.start()
    
time.sleep(5)
    
########################################################################
#
#   Code for testing ListGroupServer
#
########################################################################
#import socketserver
#from pbroker import ListGroupServer
#
#PORT = 8000
#
#class MyTCPHandler(socketserver.BaseRequestHandler):
#    def handle(self):
#        # self.request is the TCP socket connected to the client
#        self.data = self.request.recv(1024).strip()
#        print("{} wrote:".format(self.client_address[0]))
#        print(self.data
