import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def get_readable_file_size(size_in_bytes):
    if (size_in_bytes == 0):
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_in_bytes / p, 2)
    return '{0} {1}'.format(s, size_name[i])

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def load_compas_data():
    # data from https://github.com/propublica/compas-analysis
    data = pd.DataFrame.from_csv('data/Compas/compas-scores-two-years
