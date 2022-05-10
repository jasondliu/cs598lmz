import lzma
lzma.LZMACompressor(format=lzma.FORMAT_XZ)
import pyximport
pyximport.install()
from .compress_xz import lzma_compressor
from .compress_xz import LZMACompressor
import io
import os
import platform
from multiprocessing import Pool, Process, Queue, freeze_support
from multiprocessing.managers import BaseManager

def writer(outfile, data, queue, key):
    with outfile.open("wb") as fd:
        queue.get() # wait for reader to be ready
        fd.write(data)
    queue.put(key) # signal job completion

def reader(infile, queue, key):
    with infile.open("rb") as fd:
        queue.put(key) # signal writer that we're ready
        queue.get() # wait for writer to be ready
        data = fd.read()
    queue.put(data) # signal job completion


class IFile:
    # The number of bytes to return for the file size
