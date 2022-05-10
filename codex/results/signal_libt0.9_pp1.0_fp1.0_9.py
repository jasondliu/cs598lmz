import signal
signal.signal(signal.SIGINT, signal_handler)



for process in processes:
    process.join()
