import select
# Test select.select function

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9999))
s.listen(5)

while True:
    for i in select.select([s], [], [], 1)[0]:
        conn, addr = i.accept()
        print "Connceted by", addr
        print dir(i)
        time.sleep(1)
</code>

