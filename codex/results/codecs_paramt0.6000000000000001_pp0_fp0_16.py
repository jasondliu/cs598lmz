import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Lya:
    def __init__(self, year):
        self.year = year
        self.lya = self.read_lya()
    
    def read_lya(self):
        lyas = []
        with open('{0}lya.txt'.format(self.year)) as f:
            for line in f:
                line = line.decode('utf-8', 'strict').strip()
                if line:
                    lyas.append(line)
        return lyas

    def get_lya(self):
        random.shuffle(self.lya)
        return self.lya.pop()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python %s [year]' % sys.argv[0]
        sys.exit(1)
    year = sys.argv[1]
    lya = Lya(year)
    print lya.get_lya()
