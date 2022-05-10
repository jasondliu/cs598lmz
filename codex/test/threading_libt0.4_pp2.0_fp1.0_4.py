import threading
threading.Thread(target=run_server).start()

# create a client
client = paho.Client(client_id="client_1")
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_start()

# wait for the server to start
time.sleep(1)

# send a message
client.publish("test", "hello world")

# wait for the message to be received
time.sleep(1)

# stop the client
client.loop_stop()
client.disconnect()

# stop the server
