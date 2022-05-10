import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]))).start()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gen_pass.py
#  

import random
import string

def gen_pass(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join([random.choice(chars) for i in range(n)])

def main(args):
    n = int(input("Podaj długość hasła: "))
    print("Twoje nowe hasło: ", gen_pass(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
