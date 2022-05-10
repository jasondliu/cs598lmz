import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Create a directory for the metadata
os.makedirs("metadata", exist_ok=True)

# Create a directory for the pages
os.makedirs("pages", exist_ok=True)

# Download the metadata
with open("metadata/metadata.txt", "w", encoding='utf-8') as file:
    file.write(urlopen("http://www.gutenberg.org/cache/epub/feeds/rdf-files.tar.bz2").read().decode("utf-8", 'replace_with_space'))

# Extract the metadata
with tarfile.open("metadata/metadata.txt") as tar:
    tar.extractall("metadata/")

# Parse the metadata
with open("metadata/cache/epub/feeds/rdf-files.tar.bz2", "r", encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the interesting links
links = soup.find_all("a",
