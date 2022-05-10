import mmap


class DocumentCache:
    # 文件的32位的ID占4个字节， 
    doc_meta_size = 4 + 4 + 8
    doc_meta_format = "iiQ"


    @staticmethod
    def get_doc_path(dir, doc_id):
        doc_dir = join(dir, "docs")
        if not os.path.isdir(doc_dir):
            os.mkdir(doc_dir)

        return join(doc_dir, "%d" % doc_id)


    @staticmethod
    def get_doc_meta_path(dir, doc_id):
        doc_dir = join(join(dir, "meta"))
        if not os.path.isdir(doc_dir):
            os.mkdir(doc_dir)

        # return join(doc_dir, "%d" % doc_id)
        return doc_dir


    def __init__(self, dir):
        self.dir = dir

    
