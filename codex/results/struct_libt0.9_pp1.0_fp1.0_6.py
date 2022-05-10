import _struct

from myhdl import intbv, always_comb, always, instance, Signal, \
                  delay, StopSimulation
from math import log
from FilterBase import FilterBase
from utils import logical_and_reduce as LAND
from utils import logical_and_reduce as LOR

__all__ = ['PolyphaseFilterBankInt']

class PolyphaseFilterBankInt(FilterBase):
    def __init__(self, filter, tap=0):
        
        FilterBase.__init__(self, filter, tap)
        self.num_bits = len(filter)
        self.num_poly = (self.num_bits / (self.filter_len * self.num_coefs))
        self.out_type = intbv(0, min=-2**(self.num_poly * self.num_coefs),
                                max=2**(self.num_poly * self.num_coefs))
        
    def __call__(self, input, output):
        polyphase_filter = _struct.PolyphaseFilterBank(self.
