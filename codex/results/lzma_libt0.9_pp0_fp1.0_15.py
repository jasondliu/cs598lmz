import lzma
lzma.decompress(open("data/kivytest.txt", "rb").read()).decode()

print("------------------------------")

def xzdecode(f):
	fh = subprocess.Popen(["xz", "--decompress", "--stdout"], stdin=f, stdout=subprocess.PIPE)
	with fh.stdout:
		print(fh.stdout.read())

with open("data/kivytest.txt.xz", "rb") as f:
	xzdecode(f)

print("------------------------------")

bytestring = lzma.compress(b"I'm not a little teapot")

decomp = lzma.decompress(bytestring)

print(decomp)

'''

# Dictionary
def task_dictencode():
	"""lzma.encoder: Encode a file by using a static dictionary."""
	data = open("fixtures/encoder_input.txt", "rb").read()
	encoder
