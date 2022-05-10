import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# if run without args, start with accessToken copied from config
if len(sys.argv) < 2:
  try:
    sys.argv.append(config.testToken.group(1))
  except:
    pass

# Get accessToken from command-line
parser = argparse.ArgumentParser(description='Test JSON-RPC access over TCP.')
parser.add_argument("accessToken", help="A valid accessToken.")
parser.add_argument('--host', dest='host', default='127.0.0.1', help='host to connect to (default: 127.0.0.1)')
parser.add_argument('--port', dest='port', type=int, default=config.tcpPort, help='port to connect to (default: ' + str(config.tcpPort) + ')')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((args.host
