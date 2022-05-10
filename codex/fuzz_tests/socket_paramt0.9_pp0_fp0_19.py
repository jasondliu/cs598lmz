import socket
socket.if_indextoname('58')

'enp0s9'
iptables is maintained:
cat /etc/sysconfig/iptables | \
sed 's/^-A INPUT -i eth1/#-A INPUT -i eth1/g' | \
sed 's/^-A INPUT -i eth1/#-A INPUT -i eth1/g' | \
sed 's/^-A INPUT -i eth1/#-A INPUT -i eth1/g' | \
sed 's/^-A INPUT -i eth1/#-A INPUT -i eth1/g' | \
sed 's/^-A INPUT -i eth1/#-A INPUT -i eth1/g' > \
/tmp/iptables.new
mv /tmp/iptables.new /etc/sysconfig/iptables
service iptables reload
"apt-get install iptables-persistent"- choses both, active and save
"apt-get install -y iptables-persistent netfilter-persistent" -chose only activet
Now add a rule by running:
