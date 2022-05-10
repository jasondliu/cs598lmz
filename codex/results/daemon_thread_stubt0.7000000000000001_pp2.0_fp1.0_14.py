import sys, threading

def run():
    global args
    # set the flags
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.daemon:
        daemonize()

    # create the server and the event loop
    loop = asyncio.get_event_loop()
    loop.set_debug(args.debug)
    logging.info("Creating server")
    server = EchoServer(loop)
    # Create the server task
    logging.info("Starting server")
    server_task = loop.create_task(server.run_forever())
    # Run the event loop
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt")
    finally:
        # Dont forget to close the server
        logging.info("Closing the server")
        server.
