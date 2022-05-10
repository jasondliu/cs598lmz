import select
# Test select.select()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))
s.setblocking(0)
print "Connected to localhost:10000"

while 1:
    r, w, e = select.select([s],[],[],5.0)
    if len(r) != 0:
        data = s.recv(1024)
        print "data received: %s" % data
    else:
        print "I didn't receive anything"
    time.sleep(2.0)

s.close()
</code>

