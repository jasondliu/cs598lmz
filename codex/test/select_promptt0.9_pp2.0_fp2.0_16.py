import select
# Test select.select function

# output list
out = []


def write_chunck(sock):
    sock.send('hello world')
    out.append(sock)
