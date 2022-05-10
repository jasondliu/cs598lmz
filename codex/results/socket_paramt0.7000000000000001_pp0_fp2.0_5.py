import socket
socket.if_indextoname('5')

# 输出网卡名称及其索引，按照索引排序
for index, name in sorted(((index, socket.if_indextoname(index))
                           for index in socket.if_indices()),
                          key=lambda x: x[0]):
    print index, name
