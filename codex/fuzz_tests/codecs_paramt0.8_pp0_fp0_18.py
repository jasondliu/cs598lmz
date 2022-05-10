import codecs
codecs.register_error('strict', codecs.ignore_errors)


def process_web_page(data):
    '''
    Trim entire web page to just the part between the markers
    '''

    start_marker = '<!-- Begin Content -->'
    end_marker = '<!-- End Content -->'

    data = data.replace('\r\n', '\n')
    data = data.replace('\r', '\n')
    data = data.replace('\n', '{NEWLINE}')

    lines = data.split('{NEWLINE}')
    for i, line in enumerate(lines):
        if start_marker in line:
            start = i
        if end_marker in line:
            end = i

    data = '{NEWLINE}'.join(lines[start:end + 1]).strip()
    data = data.replace('{NEWLINE}', '\n')

    return data


def read_title_body(data):
    '''
    Extract title and body text from the data
    '''

    body = []

    data
