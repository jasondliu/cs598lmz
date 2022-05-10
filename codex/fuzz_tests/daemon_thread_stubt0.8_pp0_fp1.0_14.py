import sys, threading

def run():

    from twisted.web.server import Site
    from twisted.web.static import File
    from twisted.internet import reactor

    root = File(os.environ.get('DYNAMIC_PATTERN_ROOT', '.'))
    reactor.listenTCP(8080, Site(root))
    reactor.run()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()
time.sleep(2)
