import sys, threading

def run():
    # Create the server
    server = Server()
    
    # Create a new user
    user = User(server, "test")
    
    # Create a new room
    room = Room(server, "test")
    user.join(room)
    
    # Create a server event loop
    server.loop()

def test():
    # Create a client
    client = Client()
    client.send("test")

t = threading.T
