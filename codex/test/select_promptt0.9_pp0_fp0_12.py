import select
# Test select.select() for readable and writable

port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(5)

if(True):
    readable, writable, exceptional = select.select([s], [], [], 15)   # a little *long* timeout
