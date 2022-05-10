import threading
threading.stack_size(32768)


def main():
    if len(sys.argv) != 4:
        sys.exit('Usage: %s <port> <numprocs> <secret>' % sys.argv[0])
    port, numprocs, secret = [int(x) for x in sys.argv[1:]]
    if port < 1024 or port > 65535:
        sys.exit('Port must be between 1024 and 65535')
    if numprocs < 1 or numprocs > 100:
        sys.exit('Numprocs must be between 1 and 100')
    if len(secret) != 32:
        sys.exit('Secret must be 32 bytes long')

    server = Server('localhost', port, numprocs, secret)
    server.start()
    server.wait()


if __name__ == '__main__':
    main()
