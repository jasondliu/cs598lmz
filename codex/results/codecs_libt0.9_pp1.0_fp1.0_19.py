import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

with open(sys.argv[1], "r") as f:
	for line in f:
		line = line.split("|")
		filename = line[0]
		filepath = line[1]
		filename = os.path.splitext(os.path.basename(filename))[0]
		print filepath
		subprocess.call(["unrar", "x", os.path.join(filepath, filename+".rar"), KITAPLAR_KLASORU])
