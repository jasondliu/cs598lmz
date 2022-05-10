import socket
import threading
import sys
import person_pb2
import time

# Global variables


# Create person object
person = person_pb2.Person()

# Initialize person object
person.id = 1234
person.name = "Doung"
person.email = "Doung@gmail.com"
phone_number = person.phones.add()
phone_number.number = "123456789"
phone_number.type = person_pb2.Person.HOME

# Generate protocol buffers
serialize_person = person.SerializeToString()

# Initialize address
ADDR = ('localhost', 9999)


# Define socket
s_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect socket
s_connect.connect(ADDR)


# Main
def main():
    # Generate welcome screen

    print("""
        Welcome to Protocol Buffer Client!
    
            - Type 'exit' for exit program
    """)

    # Start looping

