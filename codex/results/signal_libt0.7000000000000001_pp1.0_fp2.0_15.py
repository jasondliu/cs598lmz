import signal
signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser(description='Woa!')
parser.add_argument('-ip', '--ip', type=str, help='IP Address')
parser.add_argument('-p', '--port', type=int, help='Port')
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((args.ip, args.port))

try:
    start = time.time()
    while True:
        buffer_size = random.randint(1, 1024)
        s.send(b'A' * buffer_size)
        data = s.recv(1024)
        print("%s:%d -> %s:%d [%d]" % (s.getsockname()[0], s.getsockname()[1], args.ip, args.port, buffer_size))
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nTotal:
