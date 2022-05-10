import lzma
lzma.LZMADecompressor()

# -----------------------------------------------------------------------------
# Find top-level project directory

with open(os.path.join('.', 'config', 'project.yaml'), 'r') as f:
	r = yaml.load(f)
project = r['project']

# -----------------------------------------------------------------------------
# Parse file

def parse_file (path, args, version='dev'):

	full_path = os.path.join('.hinted', version, path)

	with open(full_path, 'r') as f:
		data = f.read()

	data = tok.process(data, strip_lines=True)
	new_lines = []

	for line in data.split('\n'):
		if not '@require' in line:
			new_lines.append(line)
			continue

		require = line.split('@require')[1].strip().split(' ')[0]
		require_path = os.path.join(os.path.split(full_path)[0], require
