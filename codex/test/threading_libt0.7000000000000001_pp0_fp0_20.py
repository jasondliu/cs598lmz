import threading
threading.currentThread().setName('main')

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
    datefmt='%Y/%b/%d %H:%M:%S')
logging.info('Start')

def test(sleep_secs):
    logger = logging.getLogger(
        '%s.%s' % (threading.currentThread().getName(), test.__name__))
    logger.info('Start')
    time.sleep(sleep_secs)
    logger.info('Stop')

test(5)
logging.info('Stop')
