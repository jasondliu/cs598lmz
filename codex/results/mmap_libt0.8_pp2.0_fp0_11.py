import mmap
import os

def load_embeddings(file="model_sem.bin"):
    embeddings = {}
    with open(file, "rb") as f:
        data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        header = numpy.frombuffer(data, dtype=numpy.int32, count=3)
        num_embeddings = header[0]
        embedding_size = header[2]
        print('num_embeddings: %d, embedding_size: %d' % (num_embeddings, embedding_size))
        binary_len = numpy.dtype('float32').itemsize * embedding_size
        for i in range(num_embeddings):
            word = ""
            while True:
                ch = chr(data.read_byte())
                if ch == "\n":
                    break
                word += ch
            embedding = numpy.frombuffer(data, dtype=numpy.float32, count=embedding_size)
           
