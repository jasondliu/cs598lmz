import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b]2;' + input() + '\x07')).start()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time

os.system('clear')

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
#ubah angka 0.2 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('\033[1;32mSelamat datang di Tools saya')
mengetik('\033[1;32mSilahkan pilih tools yang mau digunakan')
mengetik('\033[1;32mKetik nomor 1
