import codecs
codecs.register_error('surrogateescape', codecs.surrogateescape_error)

from ws4py.client.threadedclient import WebSocketClient


class DummyClient(WebSocketClient):
    def opened(self):
        def data_provider():
            for i in range(1, 200, 25):
                yield "#" * i

        self.send(data_provider())

        for i in range(0, 200, 25):
            print(str(i) + ' bytes sent')
            time.sleep(0.1)

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print(m)
        if len(m) == 175:
            self.close(reason='Bye bye')


if __name__ == '__main__':
    try:
        ws = DummyClient('ws://localhost:9000/', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInter
