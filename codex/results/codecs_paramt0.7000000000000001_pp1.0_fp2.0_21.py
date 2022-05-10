import codecs
codecs.register_error('ignore', codecs.lookup('UTF-8'))

class Index(object):

    def __init__(self):
        self.index = {}
        self.doc_info = {}
        self.doc_length = {}

    def get_index(self):
        return self.index
    
    def get_doc_info(self):
        return self.doc_info

    def get_doc_length(self):
        return self.doc_length

    def create_index(self, file_name):
        """
        Create the index of the documents
        """
        f = codecs.open(file_name, 'r', 'UTF-8')
        lines = f.readlines()
        doc_id = 1
        for line in lines:
            line = line.strip('\n')
            line = line.lower()
            terms = line.split()
            count = 0
            for term in terms:
                if term in self.index:
                    if doc_id in self.index[term]:
                        self.index[term][doc_id] += 1
