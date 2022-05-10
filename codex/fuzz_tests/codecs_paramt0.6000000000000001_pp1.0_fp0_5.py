import codecs
codecs.register_error('surrogate_or_unknown',
                      lambda e: codecs.lookup_error('surrogateescape' if e.reason == 'surrogateescape' else 'replace'))

def list_files(path):
	files = []
	for (dirpath, dirnames, filenames) in os.walk(path):
		for file in filenames:
			if file.endswith('.html'):
				files.append(os.path.join(dirpath, file))
	return files

def read_file(path):
	with codecs.open(path, 'r', 'utf-8', 'surrogate_or_unknown') as file:
		return file.read()

def get_link_list(html):
	link_list = []
	for link in re.findall(r'<a href="(.+?)"', html):
		link_list.append(link)
	return link_list

def get_file_list(html):
	file_list = []
	for file in
