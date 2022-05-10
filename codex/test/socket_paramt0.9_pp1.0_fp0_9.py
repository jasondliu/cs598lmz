import socket
socket.if_indextoname(3)
socket.gethostname();





#Function to copy a file
import shutil
shutil.copy('/etc/lsb-release', '/support/')

#Function to copy folder 
shutil.copytree('/var/log/wtmp', '/support/')


#Function to create & remove a directory
import os
os.mkdir('/support')
os.rmdir('/support')

#Funciton to change directory
os.chdir('/support')

#Function to find the list of files
os.listdir()


#Print the FQDN of the local machine
machine_name=socket.gethostname()
