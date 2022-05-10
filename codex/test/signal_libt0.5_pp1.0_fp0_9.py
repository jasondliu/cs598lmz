import signal
signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
