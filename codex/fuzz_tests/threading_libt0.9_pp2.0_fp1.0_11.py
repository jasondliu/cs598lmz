import threading
threading.Thread.daemon = False

import zmq


class ClientServer(Handler):

    def get_subclasses(self):
        return [ServerReceiver, ServerSender]


class ServerReceiver(Handler):

    '''
    There will be one of these per server as well. It receives data from the
    client and sends it to the serverWorker.
    '''

    def __init__(self, client, public_endpoint, out_socket_type,
                 in_socket_type=zmq.PAIR, io_threads=1, hwm=None):
        super(ServerReceiver, self).__init__(client)

        self.context = client.context
        self.public_endpoint = public_endpoint
        self.in_socket_type = in_socket_type
        self.io_threads = io_threads
        self.hwm = hwm

        self.poller = zmq.Poller()

        self.server_receiver = self.context.socket(in_socket_type)
        self.server_
