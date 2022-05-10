import socket
# Test socket.if_indextoname()
# This check is skipped if running under travis-ci, because travis-ci uses IPv6
# without IPv6 loopback.
if os.getenv('TRAVIS') not in ('true', 'TRUE'):
    socket.if_indextoname(socket.if_nametoindex('lo'))

sys.path.append('../python')
import paho.mqtt.client as mqtt

class test_context:

    def __init__(self, args):
        self.check_args(args)
        self.check_env()
        self.validate_args()

    def check_args(self, args):
        parser = argparse.ArgumentParser()

        parser.add_argument('-p', '--port', help='Port to listen on.', default=1883, type=int)
        parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
        parser.add_argument('-i', '--use-ipv6', help='Use IPv6', action='store
