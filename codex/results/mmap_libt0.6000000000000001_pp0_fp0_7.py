import mmap

def get_size(filename):
    st = os.stat(filename)
    return st.st_size

def get_size_mmap(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem

def get_size_pysam(filename):
    import pysam
    f = pysam.AlignmentFile(filename, "rb")
    return len(list(f))

def get_size_pysam_iter(filename):
    import pysam
    f = pysam.AlignmentFile(filename, "rb")
    return sum(1 for line in f)
