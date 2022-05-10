import types
types.ModuleType('jpype')
sys.modules['jpype'] = None
sys.modules['jpype._jclass'] = None
sys.modules['jpype.awt'] = None

class Client:
    def __init__(self, broker='localhost',port=5672):
        self.broker=broker
        self.port=port
        self.exchange= 'images'
        self.queue= 'temp'

        credentials= pika.PlainCredentials('guest', 'guest')
        parameters= pika.ConnectionParameters(self.broker, self.port, '/', credentials)
        self.connection=pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='direct', passive=False, durable=True, auto_delete=False)
        self.channel.queue_declare(queue=self.queue, durable=True)
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue
