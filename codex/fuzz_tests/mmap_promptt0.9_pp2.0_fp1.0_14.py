import mmap
# Test mmap.mmap
class MapFirst(object):
    def __init__(self):
        with open('./src/urls.txt','rU') as f:
            n = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            lines = 0
            readline = n.readline
            while readline():
                lines += 1
            n.close()
        with open('./src/urls.txt','rwU') as f:
            n = mmap.mmap(f.fileno(), lines*500, access=mmap.ACCESS_READ)
            self.array = []
            readline = n.readline
            while 1:
                line = readline()
                if not line:
                    break
                tmp = line.split(' ')
                if len(tmp) >= 2:
                    self.array.append(tmp[1])
                    #print tmp[1]
        n.close()
    def search(self,key):
        for i in self.array:
            if i == key:
                return True
