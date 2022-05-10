import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# SOCKS5 proxy settings
PROXY_HOST = '127.0.0.1'
PROXY_PORT = 1086

with Controller.from_port(port = PROXY_PORT) as controller:
    try:
        controller.authenticate()
    except Exception as e:    
        print('*** Authentication failed: {}'.format(e))
        sys.exit(1)

    # check if Tor is running
    if not controller.is_authenticated():
        print('Tor is not running')
    else:
        print('Tor is running')

    """create a Hidden Service
    HS_PORT = 7778
    HS_DIR = './hidden_service'

    # generate a private key
    private_key = controller.create_hidden_service(HS_DIR, 80, target_port = HS_PORT)
    print('Private Key:\n{}'.format(private_key))
    """
