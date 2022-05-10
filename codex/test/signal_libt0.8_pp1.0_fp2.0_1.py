import signal
signal.signal(signal.SIGINT, signal_handler)

urls = (
        "/", "index",
        "/resources", "resources",
        "/test", "test"
        )
