import socket
socket.if_indextoname(socket.if_nametoindex('eth1'))
</code>
My problem is, is there a way to have the network interfaces with the name eth0-eth2, instead of them being sequentially numbered?
The reason behind this question is that I have a piece of code written for linux, and I want it to run on freebsd as well, now, in the linux version, I have a check in the beginning to see if the interfaces are sequentially numbered. Now the piece of code to check is the following, and I would like to know how to write a similar one for FreeBSD:
<code>    #check if all network interfaces are named eth0-eth3
    num_interfaces = 0
    while num_interfaces &lt;= 3:
        try:
            name = "eth" + str(num_interfaces)
            i = netifaces.ifaddresses(name).get(netifaces.AF_INET)
            print i
        except:
            print "there is no interface with the name: " + name
            sys.exit()
        num_interfaces += 1
</code>
​


