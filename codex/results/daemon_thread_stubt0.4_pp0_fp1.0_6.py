import sys, threading

def run():
    print "In run"
    print "sys.argv", sys.argv
    if len(sys.argv) < 2:
        print "Usage: python %s <port>" % sys.argv[0]
        sys.exit(1)
    port = int(sys.argv[1])
    server = SimpleXMLRPCServer(("localhost", port))
    server.register_function(pow)
    server.register_function(lambda x,y: x+y, 'add')
    server.serve_forever()

def main():
    t = threading.Thread(target=run)
    t.start()
    print "In main"
    print "sys.argv", sys.argv
    if len(sys.argv) < 2:
        print "Usage: python %s <port>" % sys.argv[0]
        sys.exit(1)
    port = int(sys.argv[1])
    proxy = xmlrpclib.ServerProxy("http://localhost:%d" % port)
    print "
