import lzma
# Test LZMADecompressor class
comp = lzma.LZMADecompressor()
with lzma.open('data/enwik8.xz', mode='r') as f:
    file_content = f.read()
text = comp.decompress(file_content).decode('UTF-8')
len(text), text[:100]

class CMUDict():
    def __init__(self, dictionary_file):
        """Load the pronunciation dictionary in the self.pronunciations."""
        self.pronunciations = {}
        for line in open(dictionary_file, 'r'):
            if line.startswith(';'): # parse lines beginning with ';' as comments
                continue
            cmu_dict_pron, _, phones_str = line.split(None, 2)
            if len(phones_str.split()) == 0: # ignore words with no pronunciations
                continue
            phones = tuple(phones_str.split()) # treat each pronunciation as a tuple of phones
            if cmu_dict_pron not in self.pronunciations: # add to dict
