import gc, weakref

from scitbx.array_family import flex # import dependency

import boost_adaptbx
ext = boost_adaptbx.import_ext("mmtbx_tls_ext")

from scitbx.array_family import flex
if(flex.double.size_type == flex.size_t):
  cctbx_size_t = "long long"
else:
  cctbx_size_t = "int"

class tls_curve_fit(ext.tls_curve_fit):

  def __init__(self, stol_0, rates):
    assert len(stol_0) == 1
    assert len(rates) == len(stol_0)
    ext.tls_curve_fit.__init__(self, stol_0, rates)

  def stol_vs_rate(self):
    return self.stols, self.rates

  def stol_for_rate(self, rate):
    return self.tls_lsq_stol_for_rate(rate)
