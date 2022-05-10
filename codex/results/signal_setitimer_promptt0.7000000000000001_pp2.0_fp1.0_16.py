import signal
# Test signal.setitimer
def handler(signum, frame):
    print "Hello World"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass
# Test socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.baidu.com", 80))

s.send("GET / HTTP/1.0\r\n\r\n")

while True:
    d = s.recv(1024)

    if d:
        print d
    else:
        break
# Test urllib2
print urllib2.urlopen("http://www.baidu.com").read()
# Test json
print json.dumps({"a":1, "b":2})
# Test os.fork
def child():
    print "Hello from child", os.getpid()
    os._exit(0)

def parent():
    while True:
        newpid = os.
