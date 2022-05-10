from lzma import LZMADecompressor
LZMADecompressor()
</code>
Result as below:
<code>Error: Compressed data is corrupt</code>
But if I use same file, open it with lzma and decompress it directly by following code:
<code>import lzma

with lzma.open("lzma_test_file", "rb") as lzma_file:
    content = lzma_file.read()
</code>
Then content is exactly what I expect. This drove me crazy as I don't understand why it's not working in my code.
I even tried to change the input file's encoding but it's also not working. 
Here is the full code:
<code>#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import io
import requests
import time
from lzma import LZMADecompressor

request_url = "https://crl.pki.goog/GTSGIAG3.crl"


def get_crl(url):
    start = time.time()
    response
