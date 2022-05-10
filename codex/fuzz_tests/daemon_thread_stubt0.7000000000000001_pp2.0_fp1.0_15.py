import sys, threading

def run():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s (%(threadName)-2s) %(message)s',
                        )
    def worker(monitor):
        logging.debug('starting')
        with monitor:
            time.sleep(0.5)
            logging.debug('Exiting')

    def service():
        logging.debug('starting')
        time.sleep(0.3)
        logging.debug('Exiting')


    monitor = threading.Lock()

    s = threading.Thread(name='service', target=service)
    w = threading.Thread(name='worker', target=worker, args=(monitor,))

    w2 = threading.Thread(target=worker, args=(monitor,)) # use default name

    w.start()
    w2.start()
    s.start()

run()
