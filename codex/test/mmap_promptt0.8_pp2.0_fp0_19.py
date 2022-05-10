import mmap
# Test mmap.mmap with a file greater than 2Gb
# http://code.google.com/p/google-app-engine-samples/source/browse/trunk/largefile/largefile.py

# assuming that DATA_FILE contains only ascii characters, strip high bit
# & convert to a string
def read_data(DATA_FILE):
    f = open(DATA_FILE, 'r')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    try:
        return m.read().translate(None, '\000')
    finally:
        m.close()

def search_data(data, query):
    results = []
    for i in xrange(len(data)):
        if data.startswith(query, i):
            results.append(i)
    return results

if __name__ == "__main__":
    DATA_FILE = '/home/peiqin/Downloads/MSR2013/test.txt'
    QUERY_FILE = 'pat'
    
