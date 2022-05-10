import mmap
import textwrap

class Error(Exception):
  pass

def _load_dict(filename, encoding="utf8"):
  """
  Load the dictionary from the file specified by filename.
  
  Parameters
  ----------
  filename : str
    The file containing the dictionary

  Returns
  -------
  The dictionary
  """
  with io.open(filename, encoding=encoding) as f:
    lines = f.readlines()
  f.close()
  return [l.rstrip("\r\n") for l in lines]

def _load_dict_mmap(filename, encoding="utf8"):
  """
  Load the dictionary from the file specified by filename.
  
  Parameters
  ----------
  filename : str
    The file containing the dictionary

  Returns
  -------
  The dictionary
  """
  with open(filename, "r+") as f:
    mm = mmap.mmap(f.fileno(), 0)
  f.close()
  return [l.rstrip("\r\n") for l in mm.split
