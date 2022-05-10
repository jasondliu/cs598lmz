import socket
socket.if_indextoname(3)

out = subprocess.check_output("python -V",shell=True)
print("Python version:",out)
