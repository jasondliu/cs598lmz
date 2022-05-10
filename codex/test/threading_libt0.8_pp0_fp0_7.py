import threading
threading.stack_size(67108864)

class BlockChain:
    def __init__(self):
        self.lock = threading.Lock()
        self.transactions = []
        self.chain = []
        self.create_block(previous_hash = '0')
        self.nodes = set()
        self.mine = False

    def create_block(self, previous_hash):
        with self.lock:
            block = {'index': len(self.chain) + 1,
                     'timestamp': str(datetime.datetime.now()),
                     'previous_hash' : previous_hash,
                     'transactions': self.transactions}

            self.transactions = []
            self.chain.append(block)
            return block

    def get_previous_block(self):
        return self.chain[-1]

