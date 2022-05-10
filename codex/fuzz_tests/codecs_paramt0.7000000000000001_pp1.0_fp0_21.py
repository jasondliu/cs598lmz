import codecs
codecs.register_error('strict', codecs.strict_errors)

def write_pagelist(page_list_filename, page_list):
    print('writing page list')
    with open(page_list_filename, 'w') as f:
        f.write('\n'.join(page_list))


def read_pagelist(page_list_filename):
    print('reading page list')
    with open(page_list_filename, 'r') as f:
        page_list = f.readlines()
    page_list = [page.strip() for page in page_list]
    return page_list


def write_page_list(page_list):
    page_list_filename = 'page_list.txt'
    print('writing page list')
    with open(page_list_filename, 'w') as f:
        f.write('\n'.join(page_list))


def read_page_list():
    page_list_filename = 'page_list.txt'
    print('reading page list')
    with open(page_list_filename
