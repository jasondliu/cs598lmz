import codecs
# Test codecs.register_error("ignore")
# Sample result: ========== RESTART =================
# b'12345\n'
# b'678910\n'
# b'1112131415\n'
# b'\n'
# b'1718192021\n'
# b'2223242526\n'
# b'2728293031\n'
# b'3233343536\n'
# b'3738394041\n'
# b'424344454647484950\n'


def reader(file):
    for lineno, line in enumerate(file, start=1):
        line = line.decode("utf-8", "ignore").rstrip()
        # print(line)
        yield line, lineno


class Note:
    def __init__(self):
        self.TAG = "notedast"
        self.DB_TABLE = "notes"
        self.DB_FILE = "notes.sqlite"
        self.note = ""
        self.note_id = None

        self.setup_database
