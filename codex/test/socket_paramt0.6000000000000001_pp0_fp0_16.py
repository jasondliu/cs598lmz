import socket
socket.if_indextoname(3)

# get the mac address of the interface
# ifconfig eth0 | grep HWaddr | awk '{print $5}' | sed 's/://g'

# get the ip address of the interface
# ifconfig eth0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1

# get the netmask of the interface
# ifconfig eth0 | grep "Mask" | cut -d ':' -f 4

# get the default gateway
# ip route | grep default | awk '{print $3}'

# get the dns server
# grep nameserver /etc/resolv.conf | cut -d ' ' -f 2


# get the mac address of the interface
def get_mac_addr(interface):
    cmd_str = "ifconfig " + interface + " | grep HWaddr | awk '{print $5}' | sed 's/://g'"
    process = subprocess.Popen(cmd_str, shell=True, stdout=subprocess.PIPE)
    return process.stdout
