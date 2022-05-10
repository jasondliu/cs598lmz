import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
def main(mqtt_address,mqtt_port, mqtt_topic):
    client = PahoMQTT.Client(mqtt_topic)
    client.will_set(mqtt_topic, payload="Server Stopped", qos=0, retain=False)
    client.connect(mqtt_address, mqtt_port)
    client.publish(mqtt_topic, "Server Started", qos=0, retain=False)
    client.start_loop()
