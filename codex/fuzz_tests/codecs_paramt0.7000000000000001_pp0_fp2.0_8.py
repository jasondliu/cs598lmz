import codecs
codecs.register_error('strict', codecs.ignore_errors)

def format_line(line):
    # Fix common encoding issues
    line = line.strip().lower()
    line = re.sub(r"([^\s])([\.,!?()])", r"\1 \2", line)
    line = re.sub(r"([\.,!?()])([^\s])", r"\1 \2", line)
    line = re.sub(r"([^\s])([\.,!?()])", r"\1 \2", line)
    line = re.sub(r"[^A-z0-9\.,!?()\-\s']", "", line)
    line = re.sub(r'[^\x00-\x7F]+', ' ', line)
    line = line.decode('utf-8', 'strict')
    line = line.encode('ascii', 'ignore')
    return line

def format_lines(lines):
    return [format_line(line) for line in lines]

def get_lines
