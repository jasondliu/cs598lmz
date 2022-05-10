import codecs
# Test codecs.register_error('my_latin_error', lambda msg: (u'000', msg.start + 1))
class StaticData():
    def __call__(self):
        self._init_data()
        return self

    def __getattr__(self, attr):
        if self._data.has_key(attr):
            return self._data[attr]
        raise KeyError('Undefined key: %s' % attr)
    __getitem__ = __getattr__

    def _init_data(self):
        self._data = {}
        rt, self._data['cs'] = self.parse_csv('cs.csv', 1)
        if not rt:
            print 'Error code', self._data['cs'], 'when read file cs.csv'
            sys.exit(1)
        rt, self._data['cities'] = self.parse_csv('cities.csv', 0)
        if not rt:
            print 'Error code', self._data['cities'], 'when read file cities.csv'
            sys.exit(2)
       
