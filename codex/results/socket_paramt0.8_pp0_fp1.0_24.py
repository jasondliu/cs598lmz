import socket
socket.if_indextoname(1)

# networking
import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

# threading
import threading
import time
from multiprocessing import Pool

def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))

