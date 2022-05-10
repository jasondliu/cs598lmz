import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    """Main function."""

    # Trap all uncaught exceptions.
    sys.excepthook = exception_hook

    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument("--debug", action="store_true", dest="debug",
                        default=False, help="debug logger")
    args = parser.parse_args()

    # Initialise the logger.
    setup_logger(LOGGER, args.debug)

    # Initialise the Google Earth Engine client.
    LOGGER.debug(
        "Initialising the Earth Engine client: %s",
        datetime.utcnow().isoformat())
    ee.Initialize()

    # Sit in an infinite loop polling the Earth Engine service.
    while True:
        poll_ee()
        time.sleep(POLL_INTERVAL)


def exception_hook(exctype, excvalue, exctb):
    """Exception hook."""
    LOGGER.error(
       
