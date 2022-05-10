import codecs
codecs.register_error('strict', codecs.ignore_errors)

#----------------------------------------------------------------------------
#  
#----------------------------------------------------------------------------
def load(name, encoding='utf-8'):
    lines = []
    with codecs.open(name, 'r', encoding) as f:
        for line in f:
            lines.append(line)
    return lines

#----------------------------------------------------------------------------
#  
#----------------------------------------------------------------------------
def save(name, lines, encoding='utf-8'):
    with codecs.open(name, 'w', encoding) as f:
        for line in lines:
            f.write(line)

#----------------------------------------------------------------------------
#  
#----------------------------------------------------------------------------
def read_text(name, encoding='utf-8'):
    with codecs.open(name, 'r', encoding) as f:
        text = f.read()
    return text

#----------------------------------------------------------------------------
#  
#----------------------------------------------------------------------------
def write_text(name, text, encoding='utf-8'):
    with codecs.open(name, 'w', encoding) as f:
        f.write(text)

#----------------------------------------------------------------------------

