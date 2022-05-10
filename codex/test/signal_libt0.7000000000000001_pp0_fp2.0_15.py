import signal
signal.signal(signal.SIGINT, handler)

def main():
    """The main function."""
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Bye")
        sys.exit(0)

def main_loop():
    """The main loop."""
