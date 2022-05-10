import lzma
# Test LZMADecompressor's `description` attribute
def test_description():
  assert isinstance(lzma.LZMADecompressor().description, bytes)
  # Till Python 3.8, default value for `description` was `True` instead
  # of `b""`. Hence this assertion
  assert lzma.LZMADecompressor().description in (b"", b"XZ")
def test_parallel():
  from _testcapi import get_pyconfig_var
  is_pypy = get_pyconfig_var("Py_USING_UNICODE") < 0
  if is_pypy: return
  scenario = scenario_from_path('lzma_parallel_data.lzma')
  data = b"".join(scenario.expected_output_triples())
  assert lzma.decompress(data).startswith(b"LZMA parallel sample data")
  assert lzma.LZMADecompressor().decompress(data).startswith(b"LZMA parallel sample data")
  stream = lzma
