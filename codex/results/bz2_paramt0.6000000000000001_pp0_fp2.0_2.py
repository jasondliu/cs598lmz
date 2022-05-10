from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f.read())

# $ ls -la
# total 13
# drwxr-xr-x  2 root root 4096 Feb 10  2015 .
# drwxr-xr-x 21 root root 4096 Feb 10  2015 ..
# -rw-r--r--  1 root root    6 Feb 10  2015 flag.txt
# -rw-r--r--  1 root root   42 Feb 10  2015 password.raw-md5

# $ cat flag.txt
# flag{f1ag5_ar3_4w3s0m3}

# $ cat password.raw-md5
# 938f37b4d30f9b9e9c0b22e1f1dafb1e

# $ md5sum password.raw-md5
# 938f37b4d30f9b9e9c0b22e1f1dafb1e  password.raw-md5

# $ file password.raw-md5
# password.raw-md5: bzip2 compressed data, block size = 900k


