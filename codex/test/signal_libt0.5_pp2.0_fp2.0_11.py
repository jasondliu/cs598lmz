import signal
signal.signal(signal.SIGINT, signal_handler)

# Setup the API wrapper
api = Api(access_token=access_token)

# Setup the message queue
message_queue = Queue.Queue()

# Setup the message handler
message_handler = MessageHandler(message_queue, api)
message_handler.start()

# Setup the message sender
message_sender = MessageSender(message_queue, api)
message_sender.start()

# Setup the message processor
message_processor = MessageProcessor(api)

# Setup the message listener
message_listener = MessageListener(api, message_processor)
message_listener.start()

# Setup the message printer
message_printer = MessagePrinter(message_processor)
message_printer.start()

# Block the main thread
while True:
    time.sleep(1)
