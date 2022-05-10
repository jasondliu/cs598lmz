import mmap
# Test mmap.mmap:
#m = mmap.mmap(0, mmap_size, mmap_name)
#m[0] = 'm'
#m[1] = 'm'
#m[2] = 'a'
#m.close()

#args.key = "TESTER"

# Assign the message digest hash algorithm
if args.hashtype == "sha1":
    hasher = hashlib.sha1()
elif args.hashtype == "md5":
    hasher = hashlib.md5()
elif args.hashtype == "sha224":
    hasher = hashlib.sha224()
elif args.hashtype == "sha256":
    hasher = hashlib.sha256()
elif args.hashtype == "sha384":
    hasher = hashlib.sha384()
elif args.hashtype == "sha512":
    hasher = hashlib.sha512()

# Assign the gpg key
if args.key == "TESTER":
    gpg_key = "517F3CEA"

#
