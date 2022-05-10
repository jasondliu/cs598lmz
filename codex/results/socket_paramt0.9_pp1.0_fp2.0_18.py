import socket
socket.if_indextoname("8")

# Ex. 11.18 sorting texts
s = "Hello there. It's me, Bob"
s.split(" ")
sorted(s.split(" "))

# Ex. 11.19
s = "Hello there.  It's me, Bob"
s = s.split(" ")
for i in range(len(s)):
	s[i] = s[i].rstrip(".")
	s[i] = s[i].rstrip(",")
s
