import socket
socket.if_indextoname(29)

while(True):
    print("Enter IP Address")
    print("Press q to quit the program")
    choice = input()

    if(choice == 'q'):
        print("Program shutdown requested")
        break
    #else:
    #    print("here")


    print("Enter Number of packets")
    num_pkts = input()
    num_pkts = int(num_pkts)

    print("Enter Protocol used")
    print("1: UDP")
    print("2: TCP")
    print("3: ICMP")
    protocol = input()
    protocol = int(protocol)

    if(protocol == 1):
        protocol = "UDP"
    elif(protocol == 2):
        protocol = "TCP"
    elif(protocol == 3):
        protocol = "ICMP"
    else:
        print("Incorrect value entered")


    port = 80

    message = '''T'est
    Hi............................ :)
    '''

