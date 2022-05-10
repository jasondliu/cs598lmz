import sys, threading

def run():
  server_address = ('', 1337)
  httpd = HTTPServer(server_address, Handler)
  print ('Starting server, use <Ctrl-C> to stop')
  httpd.serve_forever()

if __name__ == '__main__':
  threading.Thread(target=run).start()
  while True:
    time.sleep(1000)
    print "Server is running ..."
