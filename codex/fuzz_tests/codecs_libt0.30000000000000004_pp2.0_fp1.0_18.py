import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class TxtReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_name = os.path.splitext(self.file_name)[0]
        self.lines = []
        self.read_lines()
        self.line_count = len(self.lines)
        self.current_line_index = 0

    def read_lines(self):
        with codecs.open(self.file_path, 'r', 'utf-8') as f:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                self.lines.append(line)

    def has_next_line(self):
        return self.current_line_index < self.line_count

    def next_line(self):
        if self.has
