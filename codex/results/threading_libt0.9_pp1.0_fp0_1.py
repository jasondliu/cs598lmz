import threading
threading.stack_size(1024)

# local imports
from webapp import webapp

# Create an instance of the parser
parser = argparse.ArgumentParser(description='PionServ Server')
parser.add_argument('-p', '--port', type=int, default = 5000, help = 'port number')
parser.add_argument('-s', '--ssl', action = 'store_true', help = 'run on secure port with SSL')
parser.add_argument('-c', '--certificateFile', default = 'server.crt', type=str, help = 'certificate file for SSL')
parser.add_argument('-k', '--keyFile', default = 'server.key', type=str, help = 'key file for SSL')

# Parse the arguments
args = parser.parse_args()

certificateFile = args.certificateFile
keyFile = args.keyFile

# Create a web-app instance
app = webapp()

# Run the app
app.run( host = '0.0.0.0', port = args.port, ssl
