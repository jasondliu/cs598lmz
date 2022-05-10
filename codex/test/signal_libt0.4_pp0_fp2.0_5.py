import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#
#
#

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=5000, help="The port to listen on")
    parser.add_argument("--debug",
                        action="store_true", help="Enable debug mode")
    parser.add_argument("--threaded",
                        action="store_true", help="Enable threaded mode")
    parser.add_argument("--host",
                        default=socket.gethostname(), help="Hostname to listen on. Defaults to localhost")
    return parser.parse_args()

#
#
#

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug

