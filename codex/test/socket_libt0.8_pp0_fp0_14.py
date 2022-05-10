import socket
from http.server import HTTPServer, BaseHTTPRequestHandler


# Command Line Arguments
parser = argparse.ArgumentParser(description='Run the HTTP server')
parser.add_argument('--port', type=int, default=8000)
args = parser.parse_args()

PORT = args.port

# Setting up the Web Server


class Serv(BaseHTTPRequestHandler):
    '''
    Sets up the HTTP Server and manage information requested
    '''

    @staticmethod
    def get_contents(file_name):
        '''
        Gets the contents of the file
        '''

        # Gets the path of the file
        file_path = os.path.join(os.getcwd(), file_name)

        # Reads the file
        with open(file_path, 'r') as file:
            data = file.read()

        return data

    def do_GET(self):
        '''
        Sets up the requesrted contents
        '''

        # Find the path of the file
