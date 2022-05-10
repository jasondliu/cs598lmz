import lzma
lzma.LZMAFile

import sys


def benchmark(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(func.__name__ + ': ' + str(end - start) + ' seconds.')
    return result
  return wrapper


@benchmark
def get_text_from_bz2(path):
  with bz2.open(path, 'rb') as f:
    return f.read()


@benchmark
def get_text_from_lzma(path):
  with lzma.LZMAFile(path, 'rb') as f:
    return f.read()


def main():
  text = get_text_from_bz2(sys.argv[1])
  print(text.decode('utf-8'))


if __name__ == '__main__':
  main()
