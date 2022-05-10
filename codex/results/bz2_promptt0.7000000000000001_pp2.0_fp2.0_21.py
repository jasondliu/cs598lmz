import bz2
# Test BZ2Decompressor to decompress a file
# with bz2.BZ2Decompressor() as decompressor:
#     with open('example.bz2', 'rb') as input, open('example.txt', 'wb') as output:
#         for block in iter(lambda: input.read(100 * 1024), b''):
#             output.write(decompressor.decompress(block))

import codecs
# codecs.register(codecs.lookup('latin-1'))

import collections
# collections.Counter()

import concurrent.futures
# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     for result in executor.map(lambda x: x**2, range(1, 11)):
#         print(result)
# with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
#     for result in executor.map(lambda x: x**2, range(1, 11)):
#         print(result)
# with concurrent.futures.Process
