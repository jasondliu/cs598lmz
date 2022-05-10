import bz2
bz2.BZ2File.readline = readline

from multiprocessing import Pool
print "import done"

###############################################################################
# Load data
###############################################################################

# Load data
def load_data(file_name, path="../data/train/"):
    """
    Loads data from bz2 file
    """
    data = []
    bz_file = bz2.BZ2File(path + file_name + ".json.bz2")
    for line in bz_file:
        data.append(json.loads(line))
    bz_file.close()
    return data

print "load data"

###############################################################################
# Some statistics
###############################################################################

# Some statistics on data
def get_stat(data):
    """
    Returns some statistics on the data
    """
    bid_count = 0
    bidder_count = 0
    device_count = 0
    country_count = 0
    ip_count = 0
    url_count = 0
    bid_per_bidder =
