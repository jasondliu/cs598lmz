import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Open and read the file as a single buffer
fd = open('data/dados_brutos_novo.csv', 'r', encoding='utf-8')
data = fd.read()
fd.close()

# Replace Windows line endings with Unix
data = data.replace('\r\n', '\n')

# Replace double quotes with single quotes
data = data.replace('"', "'")

# Replace multiple newline with a single newline
data = re.sub('\n\n+', '\n', data)

# Remove Windows line endings
data = data.replace('\n', '')

# Remove empty lines
data = re.sub('\n', '', data)

# Remove empty lines
data = re.sub('\n\n+', '\n', data)

# Remove empty lines
data = re.sub('\n\n+', '\n', data)

# Remove empty lines
data = re.
