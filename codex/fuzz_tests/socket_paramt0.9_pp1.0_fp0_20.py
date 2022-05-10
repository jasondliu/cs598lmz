import socket
socket.if_indextoname(3)

# Method 2: socket.gethostbyname_ex()
socket.gethostbyname_ex('www.example.com')

# Method 3: interface objects
ins = netifaces.interfaces()
for i in ins:
    print('\n**********Details of Interface - ' + i + ' ************')
    try: # This is required as not all interfaces have linked IPs.
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

# Some network interfaces from the OS can be seen from if
