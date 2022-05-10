import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_ssize_t, ctypes.c_void_p
)

#This function is used to generate the hash of the file
def generate_hash(filename):
    with open(filename, "rb") as fh:
        data = fh.read()
        data_len = len(data)
        ctx = llvmlite.binding.ffi.new("SHA256_CTX *")
        llvmlite.binding.lib.SHA256_Init(ctx)
        llvmlite.binding.lib.SHA256_Update(ctx, data, data_len)
        digest = llvmlite.binding.ffi.new("unsigned char[]", 32)
        llvmlite.binding.lib.SHA256_Final(digest, ctx)
        #print(digest)
        digest_hex = "".join("{:02x}".format(x) for x in digest)
        #print(digest_hex)
