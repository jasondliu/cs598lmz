import codecs
codecs.register_error("strict", codecs.ignore_errors)


class UdpLoadTest(unittest.TestCase):
    def setUp(self):
        random.seed()

    def test_load(self):
        log_event.info(">>>>>>>> started UdpLoadTest <<<<<<<<")
        self._start_udp_receiver_and_checker()
        self._start_udp_sender()

    def _start_udp_sender(self):
        log_event.info("Started UDP sender")
        # set up socket
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.bind(("", 0))
        ip, port = udp_sock.getsockname()
        # get data to send
        message = b"A" * (DEFAULT_MESSAGE_SIZE - CHECKSUM_LEN)
        # send data
        packets_to_send = 10000
        t1 = self._get_milli_sec()
        for _ in
