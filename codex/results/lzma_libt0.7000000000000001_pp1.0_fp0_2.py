import lzma
lzma_codec = codecs.lookup('x-lzma')

def read_line(buf):
    # Decode the buffer using the best avaialble codec
    if zlib_codec:
        data = zlib_codec.decode(buf, 'ignore')[0]
        # Ignore empty lines and lines that have just a newline
        if data != '' and data != '\n':
            return data
    return None

class Consumer(threading.Thread):
    def __init__(self, queue, outstream, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.outstream = outstream
        self.name = name
        self.daemon = True

    def run(self):
        print("Consumer %s starting" % self.name)
        while True:
            buf = self.queue.get()
            if buf == None: # flag to stop
                break
            line = read_line(buf)
            if not line:
                print("Consumer %s: No line to read!"
