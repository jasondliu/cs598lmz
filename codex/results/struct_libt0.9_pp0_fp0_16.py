import _struct
- x = mix.invert(y)

'''

from scipy import signal

import _struct

class Mixin:

	def __init__(self):
		self.buffer = _struct.Buffer()

	def _convertSeries(self, y, rate_in, rate_out):
		if rate_in == rate_out:
			return y
		sfreq = float(rate_in)
		dfreq = float(rate_out)
		factor = dfreq / sfreq
		y = self._convertMultiply(y, factor)
		return y

	def _convertMultiply(self, y, factor):
		samples = len(y)
		if samples * factor < 1.0:
			return None
		ny = int(samples * factor)
		if ny == samples:
			return y
		x = signal.resample(y, ny)
		return x

	def convert(self, y, rate_in
