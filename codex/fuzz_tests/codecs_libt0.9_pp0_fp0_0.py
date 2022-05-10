import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 

'tokyo_cabinet.utf8coder' else None)

class udtReader :
    def __init__(self) :
        self.tb = TokyoCabinet.BDB()
        self.tb.open('../db/udt.tcb')
        self.tb.setcache(768, 768)
        self.tb.optimize()
        self.tb.settuning(self.tb.TTLNUM, 128)
        self.tb.settuning(self.tb.TXCWMAX, 1024 * 1024 * 512)
        self.tb.settuning(self.tb.TXCWMIN, 1024 * 1024 * 128)

    def close(self) :
        self.tb.close()

    def load(self, item) :
        it = cPickle.dumps(item)
        k = self.tb.get(it)
        if k is not None:
            k = cPickle.loads(k
