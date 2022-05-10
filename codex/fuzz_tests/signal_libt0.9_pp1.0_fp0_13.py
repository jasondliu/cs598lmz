import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
def main(mqtt_address,mqtt_port, mqtt_topic):
    client = PahoMQTT.Client(mqtt_topic)
    client.will_set(mqtt_topic, payload="Server Stopped", qos=0, retain=False)
    client.connect(mqtt_address, mqtt_port)
    client.publish(mqtt_topic, "Server Started", qos=0, retain=False)
    client.start_loop()
    try:
        hi = HelloWorld()
        channel = grpc.insecure_channel("localhost:50051")
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
        mqtt_msg = str(mqtt_topic) + " " + response.message
        client.publish(mqtt_topic, mqtt_msg
