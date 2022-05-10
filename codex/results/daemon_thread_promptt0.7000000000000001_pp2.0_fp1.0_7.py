import threading
# Test threading daemon

def target():
    # Create an instance of the server
    app.run(host='0.0.0.0', port=8888)

thread = threading.Thread(target=target)
thread.daemon = True
thread.start()

previous_data = ''

# Create an instance of the web browser
webbrowser.open('http://127.0.0.1:8888/', new=0, autoraise=True)


def run_server():
    app.run(host='0.0.0.0', port=8888)

### MAIN CODE ###
# Initialize the input and output thread
input_thread = threading.Thread(target=input_loop, name='input_thread')
output_thread = threading.Thread(target=output_loop, name='output_thread')

# Start the input and output thread
input_thread.start()
output_thread.start()

# Create a lock
lock = threading.Lock()

# Wait for the input and output thread to finish execution
input_thread.join()

