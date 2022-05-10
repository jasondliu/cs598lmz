import _struct
import socket
import config

server_address = (config.webserver, 3000)
BUFFER_SIZE = 65535
network = ""

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the socket to the port
sock.bind(server_address)

# Sorting function
def SortSongs(SortedSongs):
    # If it was the name, we will sort according the name so we need to switch the objects
    if SortedSongs[0] == config.sort_name:
        if SortedSongs[1] == "ASC":
            SortedSongs1 = sorted(sorted(SortedSongs[2], key=lambda song: song.Artist.lower()), key=lambda song: song.Name.lower())
        else:
            SortedSongs1 = sorted(sorted(SortedSongs[2], key=lambda song: song.Artist.lower()), key=lambda song: song.Name.lower(), reverse=True)

    # If it was
