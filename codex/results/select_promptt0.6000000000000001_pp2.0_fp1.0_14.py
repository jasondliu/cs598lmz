import select
# Test select.select()

# Select on a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))
print 'Connected'
s.setblocking(0)
print select.select([s], [], [])
s.setblocking(1)
s.close()
print 'Closed'

# Select on a file
f = open(r'C:\Windows\notepad.exe')
print select.select([f], [], [])
f.close()

# Select on a pipe
r, w = os.pipe()
print select.select([r], [], [])
os.close(r)
os.close(w)
