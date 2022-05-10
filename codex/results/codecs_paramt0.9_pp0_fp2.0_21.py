import codecs
codecs.register_error('strict', codecs.lookup_error ('strict'))

class OrderGenerator(object):
    def __init__(self, local_mapping_dir):
        self.dtf = {'en': {}, 'ru': {}, 'be': {}}
        self.nr = {'en': [], 'ru': [], 'be': []}
        self.read_dtf(local_mapping_dir)

    def read_dtf(self, local_mapping_dir):
        local_mapping_file = os.path.join(local_mapping_dir, 'dtf.txt')
        print('...reading dtf from file:', local_mapping_file)
        with codecs.open(local_mapping_file, 'r', 'utf-8-sig') as ifp_dtf:
            line_number = 1
            for line in ifp_dtf.readlines():
                line = line.split('\t')
                if line[0][0] == '#':
                    continue
                self.dtf['be'
