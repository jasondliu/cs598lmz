import lzma
lzma_compress = lzma.LZMACompressor()
writer = None
readers = {}

def writer_thread(v_args):
    while True:
        reader, data = q.get_nowait()
        q.task_done()
        try:
            reader._write_no_locking(reader, data)
        except exceptions.StreamError:
            pass

