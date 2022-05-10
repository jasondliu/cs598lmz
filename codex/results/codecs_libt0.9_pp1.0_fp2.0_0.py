import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)


class Base(object):
    def __init__(self):
        import sys, os
        self.infile = sys.argv[1]
        self.outfile = os.path.splitext(sys.argv[1])[0]+'.yml'
        self.generate()

    def parse(self):
        raise NotImplemented("Not implemented")

    def generate(self):
        with open(self.infile, 'r') as infile, open(self.outfile, 'w') as outfile:
            d = self.parse(infile)
            if d:
                yaml.dump(d, outfile, allow_unicode=True, default_flow_style=False)


class DfToYaml(Base):
    def parse(self, infile):
        for line in infile.readlines():
            if '--' in line: #TODO accept more than one --, in different positions
                fs
