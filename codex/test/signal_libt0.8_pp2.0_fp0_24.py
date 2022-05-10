import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    # Get the command line arguments
    args = parse_args()

    # Set up the logger
    logger = logging.getLogger('tracker')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Start the trackers
    trackers = []
    for trk_config in args.trk_config:
        trackers.append(PlanarTracker(trk_config))
    for trk in trackers:
        trk.start()

    # Start the bridge
    bridge = SensorBridge()

    # Add the trackers to the bridge
    for trk in trackers:
        bridge.add_tracker(trk)


