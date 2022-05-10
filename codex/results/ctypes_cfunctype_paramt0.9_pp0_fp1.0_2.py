import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def rand():
	# print "In rand()"
	return rnd.random()

def randint(i):
	return irnd.randint(0,i)


def make_noise(n):
	# noise = (noise2*2.0-1.0) # convert to -1..1
	noise = noise2(n)
	noise = noise * noise
	noise = noise - filter(noise,0.25)
	noise = noise - filter(noise,0.25)
	noise = noise - filter(noise,0.25)
	# noise = noise - filter(noise,4)
	# noise = noise - filter(noise,4)
	# noise = noise - filter(noise,4)
	return noise
def make_noise_flat(n):
	# noise = (noise2*2.0-1.0) # convert to -1..1
	noise = noise2(n)
	noise = noise * noise
	# noise
