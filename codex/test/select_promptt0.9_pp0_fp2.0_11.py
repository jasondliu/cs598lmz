import select
# Test select.select
print('select() timeout:')
rlist, wlist, xlist = select.select([sys.stdin], [], [], 1.0)
if rlist:
    input()
else:
    print('I/O timeout')
# Test select.poll()
print('\npoll() timeout:')
p = select.poll()
p.register(sys.stdin, select.POLLIN)
for i in range(5):
    events = p.poll(1000)
