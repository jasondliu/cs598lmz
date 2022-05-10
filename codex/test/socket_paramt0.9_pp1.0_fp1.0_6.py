import socket
socket.if_indextoname(2)

# Code ends here


# --------------
# Code starts here
listen_port = 6666
listen_ip='0.0.0.0'
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((listen_ip,listen_port))
while(True):
    data,addr = server.recvfrom(1024)
    print('from_ip_port {}:{}'.format(addr[0],(addr[1])))
    print('data{}'.format(data.decode()))

# Code ends here


# --------------
# Code starts here

#Function to send data
def send_data_over_socket(c_socket):
    
    #Decoding data into file name
    file_name=c_socket.recv(1024).decode()
    print('File_name :{}'.format((file_name)))
    
    #Opening the file
