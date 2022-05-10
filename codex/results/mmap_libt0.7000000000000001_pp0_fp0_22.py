import mmap

def get_time():
    return time()

def read_file(filename):
    start_time = get_time()
    with open(filename, "r") as f:
        lines = [line for line in f]
    end_time = get_time()
    return (lines, end_time - start_time)

def read_mmap(filename):
    start_time = get_time()
    with open(filename, "r") as f:
        mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        lines = mm.readlines()
    end_time = get_time()
    return (lines, end_time - start_time)

def file_len(filename):
    with open(filename, "r") as f:
        return sum(1 for line in f)

def run_tests(filename, test_count):
    print("Lines in the file: {}".format(file_len(filename)))
    file_time_sum = 0.0
    mmap_time
