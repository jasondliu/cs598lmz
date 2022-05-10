import _struct
from fit.Fit import Fit

class Struct(Fit):
    def __init__(self, s):
        Fit.__init__(self, s)
        self.s = s
        self.descriptors = self._get_descriptors()
        self.num_sub_fits = len(self.descriptors)
        self.sub_fits = [Fit(self.f[self.sub_fits_offsets[i]:self.sub_fits_offsets[i + 1]]) for i in range(self.num_sub_fits)]
    def _get_descriptors(self):
        d = [f.split() for f in self.s.split('\n') if f.find('subfits') == -1 and f.find('descriptor') != -1]
        return d[0] if len(d) > 0 else None
    @property
    def sub_fits_offsets(self):
        return [int(f) for f in self.s.split('subfits')[1].split() if f.isdigit()]
   
