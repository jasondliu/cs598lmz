import lzma
lzma_encode = lzma.LZMAEncoder('-lc3 -lp3 -pb2').encode
lzma_decode = lzma.LZMADecoder('-lc3 -lp3 -pb2').decode

import json

class ObjectEncoder(object):
    def __init__(self, filename, mode='r', verbose=True):
        self.filename = filename
        self.mode = mode
        self.verbose = verbose

    def __enter__(self):
        if verbose:
            print("Opening object file {0} in mode {1}".format(self.filename, self.mode))

        if self.mode == 'w':
            self.f = open(self.filename, 'wb')
            self.encoder = lzma.LZMAEncoder('-lc3 -lp3 -pb2')

            self.enc_stream = io.BufferedWriter(self.encoder.stream_encoder())
        else:
            self.f = open(self.filename, 'rb')
            self.dec
