import socket
socket.if_indextoname(25)

#iterate over interfaces, print their name and index
print("\n[*] Available interfaces: ")
for i in range(0, len(interfaces)):
    print("[+] " + interfaces[i].name + ": " + str(interfaces[i].description))



#iterate through available interfaces
#sniff for ethernet
for interface in interfaces:
    if interface.name == interface_name:
        print("[*] Starting sniff on interface: " + interface_name + ": " + interface.description)
        sniff(iface=interface_name, filter=filter, prn=packet_summary)
        #print sniffer(iface=interface_name, filter=filter)
