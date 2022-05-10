import sys, threading

def run():
	"""
	Run the test
	"""
	#print()
	#print("*****************************************************")
	#print("Test suite 7: inverse FFT-II ")
	#print("*****************************************************")
	print()

	# The test will process the whole input file. There is a 2000 kHz wave
	# file in the directory
	test_file = wave.open('test.wav', 'r')

	# The wave file is a the usual sound wave
	F = test_file.getframerate()
	L = test_file.getnchannels()
	s = test_file.readframes(test_file.getnframes())

	m = np.fromstring(s, dtype=np.int16)
	N = len(m)/2
	m = np.reshape(m, (N,L), order='F')
	left_channel = m[:,0]

	print("\tTest with a wave file... Left channel only")
	stdout.flush()
	e, x, y = ynii.fft_ii_run(left_channel
