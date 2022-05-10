import lzma
lzma_decompressor = lzma.LZMADecompressor()

class LZMAPipeline(threading.Thread):
  def __init__(self, buflen=100, *args, **kwargs):
    """Create a new pipeline object.

    buflen is the size of the ring buffer for data between the producer
    and consumer threads.
    """
    self._buffer = array('c', ['\0'] * BUFLEN)
    self._buflen = buflen
    self._bufmask = buflen - 1
    self._bufrd = 0
    self._bufwr = 0
    self.total_bytes_read = 0    # signals eof to consumer
    self._eof_count = 0

    self._lock = threading.Lock()
    self._evt_data_avail = threading.Event()
    self._evt_buf_space = threading.Event()
    self.compress = threading.Event()
    self.decompress = threading.Event()
    self.producer_started = threading
