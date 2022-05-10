import socket
socket.if_indextoname(3)
</code>
but if say I wanted to put netstat in that variable how would I go about doing it i did this 
<code>import socket
import subprocess
netstat = subprocess.Popen('netstat', shell=True, stdout=subprocess.PIPE).stdout.read()
int= socket.if_indextoname(netstat)
print(int)
</code>
but it didnt work 


A:

You can get list of all indexing information, which is inside <code>/sys/class/net/ &lt;interface&gt;/ifindex</code>, all will be inside a list as they are
<code>&gt;&gt;&gt; def get_indices():
...     return [ i.strip() for i in open("/sys/class/net/wlan0/ifindex").readlines() ]
...
&gt;&gt;&gt; get_indices()
['4']
</code>
Now you can use same approach to get only the first one which your interface has, as <code>index.txt</
