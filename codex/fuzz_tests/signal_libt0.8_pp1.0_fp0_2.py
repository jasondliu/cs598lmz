import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Stream to standard output
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# Execute main function
if __name__ == '__main__':
    main(sys.argv)
