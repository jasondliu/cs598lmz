import select
# Test select.select()

def reader(s):
    while 1:
        data = s.recv(1024)
