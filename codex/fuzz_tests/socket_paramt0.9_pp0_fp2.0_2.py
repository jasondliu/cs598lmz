import socket
socket.if_indextoname('1')
</code>
it should return lo if the name is not found, but if I type random string in place of an int, it will crash.
<code>Traceback (most recent call last):
  File "s.py", line 3, in &lt;module&gt;
    socket.if_indextoname('1')
TypeError: if_indextoname() argument 1 must be int, not str
</code>
I could manually check if it's an int, but is it some way to do it by default? Or do I have to keep default argument where <code>lo</code> is passed, but this value could be only used if not specified?


A:

You could just use a default argument and convert the input to an int.
<code>def if_indextoname(interface, default='lo'):
    try:
        return socket.if_indextoname(int(interface))
    except ValueError:
        return default
</code>

