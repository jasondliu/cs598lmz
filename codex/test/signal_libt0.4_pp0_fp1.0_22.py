import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a client instance
client = mqtt.Client()

# Connect to the broker
client.connect("localhost", 1883, 60)

# Start the network loop
client.loop_start()

# Publish a message
client.publish("test/topic", "Hello world!")

# Wait for a second
time.sleep(1)

# Stop the network loop
