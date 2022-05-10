import threading
# Test threading daemonic attribute

def set_daemon(d):
    if not t.is_alive():
        print "can't set daemon attribute of stopped thread"
    if d:
        t.daemon = True
    else:
        t.daemon = False

def check_daemon():
    if not t.is_alive():
        print "can't get daemon attribute of stopped thread"
    print "daemon is", t.daemon

def check_alive():
    print "alive is", t.is_alive()

def check_ident():
    if not t.is_alive():
        print "can't get ident of stopped thread"
    print "ident is", t.ident

def check_name():
    if not t.is_alive():
        print "can't get name of stopped thread"
    print "name is", t.name

def check_repr():
    if not t.is_alive():
        print "can't get repr of stopped thread"
    print "repr is", repr(t)

def set_
