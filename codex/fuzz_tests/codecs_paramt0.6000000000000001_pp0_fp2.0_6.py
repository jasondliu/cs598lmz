import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def strip(s):
    return s.strip()

def parse(s):
    return s.split(':')

def get_id(line):
    return line[0]

def get_name(line):
    return line[1]

def get_email(line):
    return line[2]

def get_phone(line):
    return line[3]

def get_address(line):
    return line[4]

def get_zip(line):
    return line[5]

def get_city(line):
    return line[6]

def get_state(line):
    return line[7]

def get_country(line):
    return line[8]

def get_lang(line):
    return line[9]

def get_login(line):
    return line[10]

def get_password(line):
    return line[11]

def get_spouse(line):
    return line[12]

def get_spouse
