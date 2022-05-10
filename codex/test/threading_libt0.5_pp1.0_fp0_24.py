import threading
threading.stack_size(20000)

# set up the connection to the server
print("connecting...")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port=port, keepalive=60)

# start the client
client.loop_start()

# wait for the connection to be established
print("waiting for connection...")
while not connected:
    time.sleep(0.25)

# subscribe to the topic
print("subscribing...")
client.subscribe(topic)

# wait for messages to be received
print("waiting for messages...")
while True:
    time.sleep(1)

# disconnect
