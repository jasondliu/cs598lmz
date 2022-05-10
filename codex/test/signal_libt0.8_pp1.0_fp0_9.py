import signal
signal.signal(signal.SIGINT, signal_handler)

ip_addr = "192.168.1.2"
listener = Listener(ip_addr)

