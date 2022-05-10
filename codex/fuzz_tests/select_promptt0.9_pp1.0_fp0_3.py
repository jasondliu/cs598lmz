import select
# Test select.select()
print('Waiting for ten seconds')
rlist, wlist, xlist = select.select([sys.stdin], [], [], 10)
if rlist:
    s = sys.stdin.readline()
    print('You said ', s)
else:
    
