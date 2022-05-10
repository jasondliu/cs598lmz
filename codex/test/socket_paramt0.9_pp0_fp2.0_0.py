import socket
socket.if_indextoname("2")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("", 12345))


i=0
while i<200:
	msg,addr = s.recvfrom(4096)
	t=datetime.datetime.now()
	filename=str(addr[0])+"_"+str(i)+"_"+str(t.hour)+"-"+str(t.minute)+"-"+str(t.second)
	f = open (filename, "w")
	f.write ('client: %s\n' %str(addr))
	f.write ('clock: %s,%s,%s\n' %(str(t.hour),str(t.minute),str(t.second)))
