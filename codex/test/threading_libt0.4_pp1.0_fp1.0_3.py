import threading
threading.stack_size(67108864)

class Server(threading.Thread):
    def __init__(self, server_address, RequestHandlerClass):
        super(Server, self).__init__()
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False

    def serve_forever(self):
        self.__is_shut_down.clear()
        self.__shutdown_request = False
        while not self.__shutdown_request:
            self.handle_request()
        self.__is_shut_down.set()

    def handle_request(self):
        request, client_address = self.get_request()
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)

