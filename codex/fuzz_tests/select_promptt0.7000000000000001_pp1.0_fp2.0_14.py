import select
# Test select.select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 0))
sock.listen(5)

port = sock.getsockname()[1]

print "Listening on port %d" % port

print "Waiting for a connection..."

conn, addr = sock.accept()
print "Got connection from", addr

# Write
print "Writing"

for i in xrange(20):
    conn.send("1234567890")
print "Wrote 20 10-byte strings"

# Read
print "Reading"

buff = ""
select.select([conn], [], [])
while True:
    data = conn.recv(20)
    if not data:
        break
    buff += data

print buff
print "Read %d bytes" % len(buff)

conn.close()
sock.close()
</code>


A:

The TCP stack (and the driver) will not send all the data at once, but only a small chunk of it
