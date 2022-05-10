import select
# Test select.select
print('Select-IO test')
while True:
    rlist, wlist, elist = select.select([sys.stdin,], [], [])
    if sys.stdin in rlist:
        input = sys.stdin.readline()
        print(input)
    else:
        print('Timeout...')


__author__ = 'liuhui'
import socket
