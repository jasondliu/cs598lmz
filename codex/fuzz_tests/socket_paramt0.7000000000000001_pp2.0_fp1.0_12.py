import socket
socket.if_indextoname(int(d['ifindex']))

def get_ifname(ifindex):
    if int(ifindex) < 0:
        return None
    for iface in netifaces.interfaces():
        for i in netifaces.ifaddresses(iface).get(netifaces.AF_LINK, []):
            if i.get('addr') == ifindex:
                return iface
    return None

ifname = get_ifname(ifindex)
iface = netifaces.ifaddresses(ifname)

iface[netifaces.AF_INET][0]

for iface in netifaces.interfaces():
    print iface, netifaces.ifaddresses(iface)


import psutil, os
def get_pid(name):
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name'])
		except psutil.NoSuchProcess:
			pass
		else:
			if name ==
