import codecs
codecs.register_error('strict', codecs.ignore_errors)

class InvertedIndex:
    def __init__(self, docs_file, index_file, skip, doc_count):
        self.docs_file = docs_file
        self.index_file = index_file
        self.skip = skip
        self.doc_count = doc_count

    def create_index(self):
        with open(self.docs_file, 'r') as f:
            for i, line in enumerate(f):
                if i % self.skip == 0:
                    split_line = line.split('\t')
                    doc_id = split_line[0]
                    doc = split_line[1]
                    doc_name = split_line[2]
                    doc_url = split_line[3]
                    doc_title = split_line[4]

                    doc_text = doc.decode('utf-8', 'strict').lower()
                    doc_text = re.sub('[^a-zA-Z0-9 ]', '', doc_text)
                    doc_text
