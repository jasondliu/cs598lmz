import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func = FUNTYPE(lambda x: x)

pSocket.sendto(b'1', ("localhost", 12345))
print(*select.select([pSocket], [], [], 0), sep="\n")
</code>
This prints:
<code>0
0
0
</code>
Linux
If I run this exact code on linux with the exact same python version, after 2.7 seconds I get:
<code>0
0
2
</code>
and then after another <code>timeout</code> seconds I get:
<code>0
0
1
</code>
And if I change the readwriteset to <code>[pSocket, pSocket]</code> I get:
<code>0
0
3
</code>
So it seems to be a 2 on windows and a 1 on linux. On windows you can't tell the difference between specific fds if you select them both, whereas on linux it seems to work.
Windows
But then on windows if I load it up on Geany (an editor) and run
