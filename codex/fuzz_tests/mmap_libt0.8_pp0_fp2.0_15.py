import mmap


class ReadFile(object):
    def __init__(self):
        pass

    def get_data(self, file):
        f = open(file, 'r')
        data = f.read()
        f.close()
        return data

    def get_data_mmap(self, file):
        fo = open(file, 'r')
        mm = mmap.mmap(fo.fileno(), 0, access=mmap.ACCESS_READ)
        data = mm.read(100)
        mm.close()
        fo.close()
        return data

    def get_data_mmap_iterate(self, file):
        fo = open(file, 'r')
        mm = mmap.mmap(fo.fileno(), 0, access=mmap.ACCESS_READ)

        for line in iter(mm.readline, ""):
            splitline = line.split(" ")
            user = splitline[0]
            timestamp = splitline[3]+" "+splitline[4]
            path = splitline[6]

            print
