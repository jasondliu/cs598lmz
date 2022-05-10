import select
# Test select.select
s = socket.socket()
s.bind(("", 0))
s.listen(3)
r = []
x = []
r, w, x = select.select([s], [], [], 0.1)
r = []
x = []
r, w, x = select.select([s], [], [], 0.1)
