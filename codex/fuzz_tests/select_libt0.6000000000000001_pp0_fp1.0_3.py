import selectors
import sys
import termios
import tty


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080,
                        help='Port to serve on.')
    parser.add_argument('--host', default='127.0.0.1',
                        help='Host to serve on.')
    parser.add_argument('--latency', type=float, default=0.1,
                        help='Simulated network latency.')
    parser.add_argument('--loss', type=float, default=0.0,
                        help='Simulated network packet loss.')
    parser.add_argument('--reorder', type=float, default=0.0,
                        help='Simulated network packet reorder.')
    parser.add_argument('--tls', action='store_true', default=False,
                        help='Use TLS for all connections.')
    parser.add_argument('--cert', type=str, default='cert.pem',
                        help='TLS certificate file.')
