import selectors

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

SEP = b':'
EOL = b'\n'

request_counter = 0
responses = {}

def next_request_id():
    global request_counter
    request_counter += 1
    return request_counter

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = connid = next_request_id()
        log.info("starting connection %d to %s" % (connid, server_addr))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
