import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def clean_text(text):
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\xa0', ' ')
    text = re.sub(r'[\s]+', ' ', text)
    return text

def parse_page(page_content, page_title):
    page_content = page_content.replace('<pre>', '<code>')
    page_content = page_content.replace('</pre>', '</code>')
    page_content = page_content.replace('<nowiki>', '<code>')
    page_content = page_content.replace('</nowiki>', '</code>')
    page_content = page_content.replace('<pre>', '<code>')
    page_content = page_content.replace('</pre>', '</code>')
    page_content = page_content.replace('<pre>', '<code>')

