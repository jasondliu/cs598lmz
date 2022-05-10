import io
class File(io.RawIOBase):
  """Represents a single (possible open) file on a remote FS. Can be used only
  as context manager (with statement). In the with statement current directory
  is changed to given. Does not change it back when closed.
  """
  def __init__(self, cluster, filename, mode='r', buffering=-1):
    self.cluster = cluster
    self.filename = filename
    self.mode = mode
    self.closed = True
    # Ignore buffering.
    if buffering >= 0:
      if not self.closed:
        self.flush()
    # Set proper directory on start / in init.
    self.pwd = self.cluster.file_exec_list(['pwd'])[0]
    self.cluster.file_exec_list(['cd', os.path.dirname(self.filename)])
    self.fd = self.cluster.file_exec_list(['cat'])[-1]

  def readable(self):
    return self.mode in ('r', 'rw', 'rb', 'rwb')

  def
