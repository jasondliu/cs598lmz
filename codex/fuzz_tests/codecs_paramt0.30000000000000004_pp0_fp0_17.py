import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def get_text_from_html(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def get_text_from_pdf(file_name):
    with open(file_name, 'rb') as f:
        pdf = pdftotext.PDF(f)
    return '\n\n'.join(pdf)

def get_text_from_docx(file_name):
    doc = docx.Document(file_name)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def get_
