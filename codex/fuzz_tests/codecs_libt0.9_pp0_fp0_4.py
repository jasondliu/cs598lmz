import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)


GATES = 5


def get_keys_and_sigresp(sig):
	keys = []
	sigresp = 0
	lowbit = False
	for i in range(0,GATES):
		if sig & 1:
			lowbit = True
		sig /= 2
		sigresp += lowbit
		keys.append(lowbit)
	#print(keys, sigresp)
	return keys, sigresp


def convert_sig(sig):
	sig = list(sig)
	#keys, sr = get_keys_and_sigresp(sig)
	#print(keys)
	out = ''
	lowbit = False
	highbit = False
	for i in range(0,3):
		lowbit = sig & 1
		sig /= 2
		highbit = sig & 1
		sig /= 2
		out += ''.
