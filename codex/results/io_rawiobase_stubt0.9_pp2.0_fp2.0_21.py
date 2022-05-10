import io
class File(io.RawIOBase):
  def __init__(self, filename):
      self.filename = filename
  def read(self, size=-1):
      with open(self.filename, 'rb') as f:
          return f.read(size)
result = File('nombre.DAT')
result

# Donde 'result' es un archivo
# binario en memoria

# Parte II)
# Definicion de la clase FileReader
import os
class Reader:
  def __init__(self, filename, files = dict()):
    self.host = files
    self.filename = filename
    if len(self.host) == 0:
      self.host[filename] = File(filename)
    if filename not in self.host:
      self.host[filename] = File(filename)
    if len(self.host) > 2:
      self.del_prev()
  
  def del_prev(self):
    l = list(self.host.keys())
    l.remove(self.filename)
    os.remove(l[0])
    self.host
