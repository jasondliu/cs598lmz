import socket
socket.if_indextoname(3)
'''

def get_ip(iface): # getting the ip-address
	ip = ifaddresses(iface)[AF_INET][0]['addr']
	return ip

def get_mac(iface): # getting the mac-address
	mac = ifaddresses(iface)[AF_LINK][0]['addr']
	return mac

def save_hosts(hosts, file_name):
	f = open(file_name, "w")
	for k in hosts.keys():
		f.write(k + "\t" + "local" + "\n")
	f.close()

def load_hosts(file_name):
	h = open(file_name)
	load_list = []
	for line in h:
		load_list.append(line.strip().split())
	return load_list

def add_to_hosts(hosts, ip, mac):
	hosts[ip] = mac
	return hosts

def get_nbr_hosts(hosts):
	nbr
