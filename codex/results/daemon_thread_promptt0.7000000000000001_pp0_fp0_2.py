import threading
# Test threading daemon
# import time


class Server:
    def __init__(self, host, port, max_client=5):
        self.__host = host
        self.__port = port
        self.__max_client = max_client
        self.__server_socket = None

    def start(self):
        try:
            self.__server_socket = socket.socket(socket.AF_INET,
                                                 socket.SOCK_STREAM)
            self.__server_socket.bind((self.__host, self.__port))
            self.__server_socket.listen(self.__max_client)
            print("Server started on {}:{}".format(self.__host,
                                                   self.__port))
        except socket.error as e:
            print("Error : {}".format(e))

    def stop(self):
        self.__server_socket.close()

    def __handle_client(self, client_socket, client_addr):
        pass

    def run(self):
        try:
            while True:
                client_
