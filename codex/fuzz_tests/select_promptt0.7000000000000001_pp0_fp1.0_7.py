import select
# Test select.select()
print('select.select():')
while True:
    print('  ', [s.getpeername() for s in ready])
    ready = select.select(rlist, wlist, xlist, 30)
    if not any([ready[0], ready[1], ready[2]]):
        print('  timed out, do some other work here')
    for s in ready[0]:
        data = s.recv(1024)
        if not data:
            print('  closing', s.getpeername())
            s.close()
            rlist.remove(s)
        else:
            print('  received "%s" from %s' % (data, s.getpeername()))
            s.send(data)
    for s in ready[2]:
        print('  exception condition on', s.getpeername())
        rlist.remove(s)
        s.close()
