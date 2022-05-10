import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

def abort(signum, frame):
    raise IOError("Pipe closed")
signal.signal(signal.SIGPIPE, abort)

for msg in sys.stdin:
    msg = msg.strip()
    m = re.match(r"^(\d+)\s+(\d+)\s+(.*)$", msg)
    if m:
        try:
            req_id, status, msg = m.groups()
            print >> sys.stderr, "<%s> %s" % (req_id, msg)
            if status == "0":
                print "OK"
            else:
                print "ERROR"
        except Exception, e:
            print >> sys.stderr, "exception: %s" % e
            print "ERROR"
    else:
        print >> sys.stderr, "can't parse message: <%s>" % msg
        print "ERROR"
