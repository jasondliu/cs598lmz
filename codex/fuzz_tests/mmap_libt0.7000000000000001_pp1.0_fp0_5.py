import mmap

#Constants and Variables
HOST = '127.0.0.1'
PORT = 60000
BUFFER_SIZE = 1024

#Create Socket and Bind
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))

#Server Listens for Connection
serverSocket.listen(1)
connection, address = serverSocket.accept()

#File Descriptor
fd = connection.fileno()

#File Object
file_object = mmap.mmap(fd, BUFFER_SIZE, access=mmap.ACCESS_WRITE)

#Write to File Object
file_object.write("Hello Python")

#Close Server Socket
serverSocket.close()
