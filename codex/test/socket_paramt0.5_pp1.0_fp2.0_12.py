import socket
socket.if_indextoname(3)

# 上面的代码会报错，因为没有给出索引值，所以会报错

# 这个函数接受一个网络接口的索引值，然后返回对应的设备名称

# 这个函数的参数和返回值都是数字，所以要把网络接口的名称转换为数字，可以使用下面的代码

socket.if_nametoindex('eth0')

# 这个函数接受一
