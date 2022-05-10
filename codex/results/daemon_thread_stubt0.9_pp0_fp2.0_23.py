import sys, threading

def run():
    client = mqtt.Client("client_%d" % os.getpid())
    client.connect("127.0.0.1", 1883, 60)
    time.sleep(1)

    start = time.time()
    client.publish("h", "hello world, 1 message ID: %s"
                   % client._client_id, qos=1)
    while True:
        client.loop()
        now = time.time()
        if now - start > 10:
            print "==" * 8
            print "client has not received a PUBACK in 10 seconds."
            print "==" * 8
            sys.exit(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    client = mqtt.Client("server_%d" % os.getpid())
    client.on_publish = lambda client, userdata, mid: time.sleep(1)
    # this is to confirm this is a bug of paho-mqtt's implementation
    #
