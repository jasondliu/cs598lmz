import threading
# Test threading daemon
def doSth():
    print "doSth ..."
    time.sleep( 5 )
    return

def fun1 ():
    print "fun1"

def fun2 ():
    print "Fun2"
    # threading.Timer(5, fun1).start()

if __name__ == "__main__":
    # threading.Timer(5, fun1).start()
    # threading.Timer(5, fun2).start()
    t = threading.Thread(target=doSth)
    t.daemon = True
    t.start()
    print "main"
    time.sleep(1)
    print "end"
