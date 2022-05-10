import socket
socket.if_indextoname(1)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("office_wifi", "wifi_password")
while not wifi.isconnected():
    pass

print(wifi.ifconfig())
</code>
In the REPL, after running the last code block, nothing happens but the code seems to exit (i.e. I'm returned to a <code>&gt;&gt;&gt; </code> prompt). If I then call <code>wifi.connect()</code> again, it says that it's already connected.
<code>&gt;&gt;&gt; wifi.connect("office_wifi", "wifi_password")
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 107] EISCONN
</code>
How can I have the REPL wait until I am connected to a wifi network before continuing? 


A:

I do not think that the REPL is
