import codecs
codecs.register_error('dis', digit_replace)

def remove_tags(value):
    return value.replace('<div class="toc-class-list"><b>','')

def remove_braces(value):
    return value.replace('{}','')

def get_docstring_value(value):
    return value.strip('\n')

def remove_local_path(value):
    return value.replace(LOCAL_PATH,'')

def pdflinks(value):
    path = "{LOCAL_PATH}/pdfs".format(LOCAL_PATH=LOCAL_PATH)
    pdfurl = PUBLIC_URL + "/pdfs/" + value
    return '<a href="{pdfurl}" target="_blank" class="pdf-link" title="View pdf">{pdf}</a>'.format(pdfurl=pdfurl, pdf=path)


def linkfile_to_value(value):
    #return
    link = re.search("(?P<domain>ftp(?:s|)|http(?:s|)):\/\/(?P<file>.*
