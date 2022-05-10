import mmap

# NIANA
import niana
#from niana import util
import util
#from niana.parser.parser_main import Parser
from parser.parser_main import Parser
#from niana.parser.parse_error import ParseError
from parser.parse_error import ParseError
import traceback

def here():
    return sys._getframe().f_back.f_code.co_name

def file_exists(file_name):
    return os.path.exists(file_name)

def write_file(file_name, lines, newline = '\n'):
    with codecs.open(file_name, 'wb', encoding='utf8') as file:
        for line in lines:
            file.write(line + newline)
    file.close()

def write_line(file_name, line, newline = '\n'):
    with codecs.open(file_name, 'wb', encoding='utf8') as file:
        file.write(line + newline)
    file.close()


