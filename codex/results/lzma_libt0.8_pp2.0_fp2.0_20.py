import lzma
lzma.LZMA_PRESET_EXTREME

def hamming_distance(str1, str2):
	return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def compute_keysize_distance(sample):
	normalized_distances = []
	for keysize in range(2,41):
		pairs = []
		for i in range(0, len(sample), keysize):
			pairs.append(sample[i:i+keysize])
		num_pairs = len(pairs) - 1
		distances = 0
		for i in range(num_pairs):
			distances += hamming_distance(pairs[i], pairs[i+1])
		normalized_distances.append((keysize, distances / keysize))
	return min(normalized_distances, key=lambda x:x[1])[0]

def transpose(cipher, keysize):
	columns = [[] for _ in range(keysize)]
	
