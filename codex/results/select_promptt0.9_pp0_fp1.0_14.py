import select
# Test select.select()
# https://docs.python.org/2/library/select.html#select.select

sock = socket.socket()
sock.bind( ('', 5555) )

sock.listen(10)

conn, addr = sock.accept()

print select.select( [conn.fileno()], [], [], 0.5)
print 'Got a connection from: ', addr

print dir(select)

CLOSE_ON_ERROR = -1

# The daedalus client for the 'lobby'
# the main menu
class Client(object):
    """The main daemon."""

    def __init__(self, ):
        pass

    def main(self):
        s = socket.socket()
        s.connect( ('', 5555) )


        while True:
            seconds = 1 #1/60
            to_be_read, writeable, excepts = select.select([s, sys.stdin.fileno()], [], [], seconds)
            data = None
            for this_sock in to_be_read:

