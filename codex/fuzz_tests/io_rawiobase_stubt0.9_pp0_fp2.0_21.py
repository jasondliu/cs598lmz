import io
class File(io.RawIOBase):
  ...
  def name(self):
    ...
    return self._name

print int(File()) # This will produce an error, as
                  # I expect 'object' to be callable
</code>

