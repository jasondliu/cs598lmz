import socket
socket.if_indextoname(1)

# 可以看到，每个网络接口都有一个唯一的数字编号，称为网络接口索引（network interface index）。
# 这个编号可以用来指定网络接口，比如创建一个绑定了特定网络接口的套接字。
# 例如，下面的代码创建了一个 UDP 套接字，并将其绑定到网络接口 1（也就是 lo）的本地
