import select
# Test select.select function
# https://docs.python.org/3.5/library/select.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    s.connect(('127.0.0.1', 80))
except socket.error as e:
    print e

read_list = [s,]
write_list = [s,]
while True:
    ready_to_read, ready_to_write, in_error = select.select(read_list, write_list, [], 5)
    if s in ready_to_read:
        data = s.recv(1024)
        if data:
            print data
        else:
            break

s.close()

print ready_to_read
print ready_to_write
print in_error
