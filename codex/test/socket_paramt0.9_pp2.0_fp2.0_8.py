import socket
socket.if_indextoname(if_index)

def if_info():
    data = scapy.utils.linux.ifaces()
    while True:
        #Prints list of networks in the system
        yn = input("Would you like a list of interfaces? (y/n): ")
        if yn.lower() == "y":
            i = 0
            for iface in data:
                i = i + 1
                print(i, iface)
            break
        elif yn.lower() == "n":
            eth = input("Enter interface name: ")
            break
        else:
            print("Answer must be 'y' or 'n'")
    while True:
        #Prompts victim IP address
        victimip = input("Victim IP: ")
        try:
            #Checks to see if IP is valid
            socket.inet_aton(victimip)
        except socket.error:
            print("IP not valid.")
            continue
        break
