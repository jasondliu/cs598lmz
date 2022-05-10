import signal
signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser(description='Woa!')
parser.add_argument('-ip', '--ip', type=str, help='IP Address')
parser.add_argument('-p', '--port', type=int, help='Port')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((args.ip, args.port))

