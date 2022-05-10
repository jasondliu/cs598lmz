import socket
socket.if_indextoname('3') 'wlan0'
</code>
and 
<code>sudo python -c "import socket; print(socket.socket.if_names[3])" 
'wlan0'
</code>
I am running Raspbian.

