import threading
threading.stack_size(2**27)

class MulServiceImpl(MulService):
    def __init__(self):
        self.lock = threading.Lock()
        self.server = Thrift.TSimpleServer(MulService.Processor(self),
                                           TSocket.TServerSocket(port=9090),
                                           TTransport.TBufferedTransportFactory(),
                                           TCompactProtocol.TCompactProtocolFactory())

    def mul(self, num1, num2):
        self.lock.acquire()
        time.sleep(2)
        print ('mul with %d and %d' % (int(num1), int(num2)))
        self.lock.release()
        return int(num1) * int(num2)
    def div(self, num1, num2):
        self.lock.acquire()
        time.sleep(2)
        print ('div with %d and %d' % (int(num1), int(num2)))
        self.lock.release()
        if num2
