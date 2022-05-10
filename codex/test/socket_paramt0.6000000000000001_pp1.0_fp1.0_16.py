import socket
socket.if_indextoname(socket.if_nametoindex(interface))

#if you want to change the mac address

subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether 00:11:22:33:44:55",shell=True)
subprocess.call("ifconfig "+interface+" up",shell=True)
