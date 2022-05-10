import socket
socket.if_indextoname('1')

a = 1
b = 2
a is b

a = 1
id(a)

import copy

b = copy.copy(a)

a is b

a = [1, 2, 3]
b = copy.copy(a)
a is b
a[0] is b[0]

a.append(4)
a[0] = 100
a
b

a = [1, 2, 3]
b = copy.deepcopy(a)
a is b
a[0] is b[0]

a.append(4)
a[0] = 100
a
b

import copy
a = [[1, 2], 3]
b = copy.copy(a)
b
a[0] is b[0]
b[0] = 200
a
b

a[0][0] = 100
a
b

a = [[1, 2], 3]
b = copy.deepcopy(a)
b
a[0] is b[0]
b[0] = 200
a
b
