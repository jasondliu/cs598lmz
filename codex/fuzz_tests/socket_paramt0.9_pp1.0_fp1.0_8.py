import socket
socket.if_indextoname(1) # 'lo'

>>> import pprint
>>> def lfunc(a):
...     print(a)
...
>>> def lexit(a):
...     print(a)
...     print(5 / 0) # Force an exception
...
>>> def lexcept(a, b, c):
...     print(a)
...     pprint.pprint(c)
...
>>> import pdb
>>> pdb.set_trace()
--Return--

>>> pdb.run('lfunc(5)', globals(), locals())
5
None
>>> pdb.runeval('[5, e, e]')
5
4
[4, 4, 4]
>>> pdb.runcall(lexit, 3)
3
> <string>(1)?()
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> pdb.runcall(lexit, 3)
3
> <string>(1)?()
--More--(y/n)? y
> <string>(1)?()
Traceback (most recent call
