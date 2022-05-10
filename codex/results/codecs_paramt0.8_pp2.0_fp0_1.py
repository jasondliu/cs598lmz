import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('replace_with'),
											lambda name: (u' ', name.start + 1))

def saveFile(path, text):
	dirs = os.path.dirname(path)
	if not os.path.exists(dirs):
		os.makedirs(dirs)

	try:
		f = codecs.open(path, 'w', 'utf-8')
		f.write(text)
	finally:
		f.close()

def createSets(files):
	"""
		Create a set from a list of files.
	"""
	content_sets = {}
	for file in files:
		content_sets[file] = set(Utils.getFileContent(file))

	return content_sets

def joinSets(sets):
	result = set()

	for s in sets:
		result.union(s)

	return result

def getConfig(section, key):
	config =
