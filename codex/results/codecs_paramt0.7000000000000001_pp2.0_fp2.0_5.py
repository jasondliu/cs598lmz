import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_repo_path():
	repo_path = os.path.dirname(os.path.realpath(__file__))
	return repo_path

def get_relative_path(path):
	repo_path = get_repo_path()
	rel_path = path.replace(repo_path, "")
	if rel_path[0] == "/":
		rel_path = rel_path[1:]
	return rel_path

def get_absolute_path(path):
	repo_path = get_repo_path()
	abs_path = os.path.join(repo_path, path)
	return abs_path

def read_file(path):
	with open(path, 'r') as f:
		content = f.read()
	return content

def write_file(path, content):
	with open(path, 'w') as f:
		f.write(content)

def read_json(path):
	content = read
