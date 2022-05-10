import sys, threading

def run():
    global config
    global s
    global world
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info('Initializing server...')
    
    config = Config('config.xml')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', config.port))
    logging.info('Initializing world...')
    world = World(config, s)
    logging.info('Done.')
    threading.Thread(target=world.tick).start()
    logging.info('Server up and running.')
    while True:
        try:
            data, addr = s.recvfrom(1024)
            logging.debug('[%s]: %s' % (str(addr), str(data)))
            threading.Thread(target=world.parse_packet, args=(data, addr)).start()
        except Exception, e:
            logging.error('%s' % e)

run()
