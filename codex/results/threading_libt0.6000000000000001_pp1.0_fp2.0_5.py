import threading
threading.stack_size(67108864)

# Set up logging
import logging
logging.basicConfig(level=logging.INFO)

# Import the server module
from server import Server

# Initalize the server
server = Server(input_filename='input.txt',
                output_filename='output.txt',
                port=8000)

# Run the server
server.run()
