import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

def get_dirs(path):
	dirs = [dir for dir in glob.glob(path) if os.path.isdir(dir)]
	return dirs

def get_files(path):
	files = [file for file in glob.glob(path + '/*') if os.path.isfile(file)]
	return files

def get_files_with_keyword(path, keyword):
	files = get_files(path)
	files_with_keyword = [file for file in files if keyword in file]
	return files_with_keyword

def read_file_as_csv(file, delimiter=','):
	file_contents = []
	with open(file, 'r') as f:
		reader = csv.reader(f, delimiter=delimiter)
		for row in reader:
			file_contents.append(row)
	return file_contents

def write_list_as_csv(list, file, delim
