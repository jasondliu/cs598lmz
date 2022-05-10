import ctypes
ctypes.cast(0, ctypes.py_object)

# now we can create the client and connect to the server
client = Client()
client.connect("tcp://localhost:5555")

# send a "message" using the function send_string
client.send_string("Hello")

# receive a "message" using the function recv_string
message = client.recv_string()
print("Received reply [", message, "]")
