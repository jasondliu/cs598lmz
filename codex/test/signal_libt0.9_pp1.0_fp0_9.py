import signal
signal.signal(signal.SIGINT, signal_handler)


def setup_logging():
    formatter = logging.Formatter(
        "[%(asctime)s %(threadName)s] " +
        "%(levelname)7s %(module)15s:%(lineno)-4d - %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(handler)


def start_proxies():
    proxy_pool = set()
    while True:
        if len(PROXY_SERVERS) == 0:
            time.sleep(3)
            continue

        server = PROXY_SERVERS.pop()

