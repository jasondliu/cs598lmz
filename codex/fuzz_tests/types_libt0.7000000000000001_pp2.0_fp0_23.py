import types
types.FunctionType = types.LambdaType

def get_cudatalist(name, cuda_path, path_to_cuda_py, read_dev=True):
  """
  Reads a cuda data list from a .txt file.
  Each line in the file must be of the form:
  "name, cuda_path, path_to_cuda_py, read_dev"
  where read_dev (optional) can be set to False to skip read_dev.
  """
  cudatalist = []
  with open(name) as f:
    for line in f:
      line = line.strip()
      if line.startswith('#'):
        continue
      name, cuda_path, path_to_cuda_py, read_dev = line.split(', ')
      read_dev = (read_dev == 'True')
      cudatalist.append((name, cuda_path, path_to_cuda_py, read_dev))
  return cudatalist

def get_cuda_info(
