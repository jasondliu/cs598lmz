import signal
signal.signal(signal.SIGINT,__quitHandler)
signal.signal(signal.SIGQUIT,__quitHandler)
signal.signal(signal.SIGABRT,__quitHandler)
signal.signal(signal.SIGTERM,__quitHandler)

sys.excepthook = __exceptionHandler

if __name__ == '__main__':

    __configParser = ConfigParser.ConfigParser()

    __configParser.read('config.ini')

    __logFile = __configParser.get('log', 'log_file')

    logging.basicConfig(filename=__logFile, level=logging.DEBUG, format='%(asctime)s %(message)s')

    logging.info('Started')

    __serverPort = __configParser.get('server', 'port')

    #__xmlrpcServer = SimpleXMLRPCServer((__serverHostname, int(__serverPort)), logRequests = False)

