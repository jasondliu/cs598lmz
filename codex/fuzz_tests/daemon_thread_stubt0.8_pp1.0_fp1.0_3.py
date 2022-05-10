import sys, threading

def run():
    i = 0
    while True:
        i += 1
        print(i)
        yield 1

t = threading.Thread(target=run)
t.start()

def on_message(unused_client, unused_userdata, message):
    print('on_message', str(message.payload), message.topic)

client = mqtt.Client()
client.on_message = on_message
client.connect('localhost', 1883, 60)
client.subscribe('test/', 1)

client.loop_forever()
