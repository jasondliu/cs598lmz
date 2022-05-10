import io
class File(io.RawIOBase):
    def __init__(self, stream):
        self.stream = stream
        self.size = 0
    def read(self, n):
        data = self.stream.read(n)
        self.size += len(data)
        return data
    def readable(self):
        return True
    def seekable(self):
        return False
  
def _download_and_extract(url, download_dir):
    filename = url.split('/')[-1]
    filepath = os.path.join(download_dir, filename)
    if not os.path.exists(filepath):
        def _progress(count, block_size, total_size):
            sys.stdout.write('\r>> Downloading %s %.1f%%' % (
                filename, float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()
        filepath, _ = urllib.request.urlretrieve(url, filepath, _progress)
        print()
        statinfo = os.stat
