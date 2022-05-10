import weakref

logger = logging.getLogger(__name__)

class JsonRpc(object):
    def __init__(self, transport, *args, **kwargs):
        super(JsonRpc, self).__init__(*args, **kwargs)
        self.transport = transport
        self.callbacks = {}

    def _call(self, method, *args):
        id = self._create_id()
        self.callbacks[id] = self._create_callback()
        logger.debug("calling %s(%s) as %s" % (method, args, id))
        self.transport.send_json({'method': method, 'params': args, 'id': id})


    def call(self, method, *args):
        def callback(request, response):
            if response.get('error'):
                raise Exception(response['error'])
            return response.get('result')
        return self._call(method, *args)

    def notify(self, method, *args):
        return self._call(method, *
