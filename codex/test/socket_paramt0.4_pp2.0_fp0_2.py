import socket
socket.if_indextoname(2)

#ifconfig eth0 down
#ifconfig eth1 up
#ifconfig eth1 down
#ifconfig eth0 up
#ifconfig eth0 10.0.0.1/24
#ifconfig eth1 10.0.0.2/24

#sudo apt-get install -y bridge-utils
#brctl addbr br0
#brctl addif br0 eth0
#brctl addif br0 eth1
#ifconfig br0 up
#ifconfig br0 10.0.0.1/24
#ifconfig eth0 0.0.0.0
#ifconfig eth1 0.0.0.0

#sudo apt-get install -y openvswitch-switch
#ovs-vsctl add-br br0
#ovs-vsctl add-port br0 eth0
#ovs-vsctl add-port br0 eth1
#ifconfig br0 10.0.0.1/24
#ifconfig eth0 0.0.0.0
#ifconfig eth1 0.0.0.0

#sudo apt-get install -
