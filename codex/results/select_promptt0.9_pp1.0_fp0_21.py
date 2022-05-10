import select
# Test select.select
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1085))
s.listen(0)
# s.setblocking(0)
timeout = 0.2
while 1:
    readable, writable, errored = select.select([s,], [], [])
    print(readable)
    print(writable)
    print(errored)
    time.sleep(1)
'''
