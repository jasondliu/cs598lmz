from bz2 import BZ2Decompressor
BZ2Decompressor

save_dir = 'G:/python/data'

mongo = MongoClient()
db = mongo['mta']
stations = db['stations']

def extract_data(s):
    _, _, _, _, _, _, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = map(int, s[:24])
    data = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]
    rest = s[24:]
    while len(rest):
        _, _, _, _, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = map(int, rest[:16])
        rest = rest[16:]
        data.extend([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9])
    return data

def download_stations
