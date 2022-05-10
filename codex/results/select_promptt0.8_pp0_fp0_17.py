import select
# Test select.select

print select.select([], [1], [], 0)[1] == [1]
print select.select([], [], [], 0) == ([], [], [])
print select.select([], [], [1], 0)[2] == [1]
print select.select([1], [], [], 0)[0] == [1]
print select.select([1], [1], [1], 0) == ([1], [1], [1])

# Test select() with a pair of sockets

print "socketpair"

s1, s2 = socket.socketpair()
s2.close()
s1.send('x')
print select.select([s1], [], [], 0.0)[0] == [s1], "select on socket, data present"
print select.select([s1], [], [], 0.0)[0] == [s1], "select on socket, data present"
s1.close()

print "poll"

p = select.poll()
p.register(s1, select.POLLIN)
print p.poll
