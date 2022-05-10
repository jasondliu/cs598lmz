import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libpredict-gfortran.dylib')

import predict

class Satellite(object):

	def __init__(self, name, tlefile, offset=0, tle=None):
		if not tle:
			self.name = name

			with open(tlefile, "r") as f:
				lines = f.read().strip().split("\n")
				lines = filter(lambda x: x.startswith(name), lines)
				lines = sorted(lines, key=lambda x: int(x.split(",")[-1]), reverse=True)
				self.tle = lines[offset]
				self.tle = "".join(self.tle.split(",")[:2])
		else:
			self.tle = tle

	def predict(self, t):
		#print self.tle
		az, el, ra, dec, lat, lon, alt = predict.predict(t
