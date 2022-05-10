import signal
signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(0))
# ================================================================== Configuration
BIND_TO_IP   = "0.0.0.0"
BIND_TO_PORT = 4444
LOGFILENAME  = 'log.txt'
# ================================================================== Config end

def on_accept(conn):
    print("Connection establised")
    pass

def on_data(conn, data):
    print("Data:", data)

def on_disconnect(connection, errno):
    print("Disconnected with errno", errno)


def setup_logging(logger):
    log_handler = logging.FileHandler(LOGFILENAME)
    log_handler.setLevel(logging.DEBUG)
    log_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: %(message)s"))
    logger.addHandler(log_handler)

def main():
    setup_
