import socket
import os
import sys

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter server IP: ")
    port = int(input("Enter port number: "))
    client.connect((host, port))

    while True:
        filename = input("Enter a file path: ")
        client.send(filename.encode())
        filesize = os.path.getsize(filename)
        file = open(filename, "rb")
        file_to_send = file.read(filesize)
        client.send(file_to_send)
        file.close()
        print("File sent successfully!")


if __name__ == "__main__":
    main()
