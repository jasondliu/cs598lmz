import mmap

def main(argv):
    f = open(argv[0], "rb")
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    # read the data into an array of strings
    data = [f.readline().split() for i in range(41)]
    data = np.asarray(data)

    # convert to an array of floats
    data = np.asarray(data).astype(np.float)

    # now do a cumulative sum to get the T_1 total flux
    data = np.cumsum(data, axis=1)

    # now shift the data to make it monotonic
    for i in range(41):
        data[i,:] = data[i,:] - np.min(data[i,:])

    # create the y-array (R)
    y = np.asarray([0.05*i for i in range(41)])

    # interpolate the data so it's on a fine grid
    x = np.linspace(0,20
