import threading
threading.Thread(target=server.serve_forever).start()

def send_message(message):
    data = json.dumps(message).encode('utf-8')
    client.send(data)
    
def on_message(message):
    message = json.loads(message)
    if message['type'] == 'message':
        print(message['text'])
    elif message['type'] == 'error':
        print(message['text'])
    elif message['type'] == 'message_history':
        print(message['text'])

def on_open():
    send_message({'type': 'connect', 'name': 'Bob'})
    send_message({'type': 'message', 'text': 'Hello'})

client = websocket.WebSocketApp('ws://localhost:8888/',
                                on_message = on_message,
                                on_open = on_open)
client.run_forever()

server.shutdown()
