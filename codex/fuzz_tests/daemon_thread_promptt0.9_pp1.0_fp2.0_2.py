import threading
# Test threading daemonizing...
def test():
    for i in range(10):
        print "Inside test"
        time.sleep(1)
t= threading.Thread(target=test)
t.daemon = True
t.start()
t.join(5)
print threading.current_thread().is_alive()
print threading.current_thread().getName()

#Test threading with function that returns a GObject loop
def test2():
    print "Inside test2"
    context = glib.MainContext()
    loop = gobject.MainLoop(context)
    loop.run()
t2= threading.Thread(target=test2)
t2.setDaemon(True)
t2.start()
print threading.enumerate()
print threading.current_thread()
print threading.current_thread().is_alive()
print threading.current_thread().getName()
