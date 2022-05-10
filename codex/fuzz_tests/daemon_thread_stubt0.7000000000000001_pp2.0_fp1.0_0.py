import sys, threading

def run():
    # The server is accessible via the localhost on port 8051.
    app.run(host='0.0.0.0', port=8051)

threading.Thread(target=run).start()

# Connect to the server.
app.connect('ws://localhost:8051/ws')

# Wait until the connection is successful.
app.wait_for_connection()

# Use the server's services.

def on_msg(**msg):
    # Incoming messages can be accessed as keyword arguments
    print(f'Received message: {json.dumps(msg)}')

app.on_msg(on_msg)

# Multiply the two numbers and return the product to the client.
def multiply(a, b):
    return a * b

app.export(multiply)

print('App is running. Press CTRL+C to quit.')

while True:
    # Call the server's multiply service with a=5 and b=3 and print the result.
    print(app.call('multiply', a=5, b=
