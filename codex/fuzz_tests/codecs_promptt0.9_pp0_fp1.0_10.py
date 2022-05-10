import codecs
# Test codecs.register_error("replace_nstk".replace_nstk)

# import unicodedata
# unicodedata.normalize("NFKD", "")
# unicodedata.normalize("NFKC", "")
# unicodedata.normalize("NFD", "")
# unicodedata.normalize("NFC", "")

class text_parser:
    def __init__(self):
        # self.db_path = "/home/vishwas/Desktop/DB/doc.db"
        self.db_path = "/home/vishwas/PycharmProjects/Stack_Auto_QA_System/db/doc.db"
        self.conn = sqlite3.connect(self.db_path)
        self.csv_path = "/home/vishwas/PycharmProjects/Stack_Auto_QA_System/db/question_ans"
        self.limit = 2500

    def token_query(self, query_type, query, query_limit=None):
        sql_stmnt = 'select * from ' + query_type + ' where
