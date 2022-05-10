import socket
socket.if_indextoname(10)

#Network Configuration
################################################################################
#Check the ip address
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)

#Detecting the OS
import os
print("Operating system: "+os.name)

#Check the process which is executing at the time
process= subprocess.check_output("ps -U root -u root -N")
print(process)

#Check the working directory
print("Current working directory "+os.getcwd())

#Process calling
import subprocess
process= subprocess.check_output("ps -U root -u root -N")
print(process)

#Check the python version
import sys
print(sys.version)

#Numpy Array
import numpy as np
a=np.zeros((1,2))
print (a)

#Set example
#Print the items which are available in a set
