import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def print_result(result):
    if result is None:
        print('No result')
    else:
        print('Result: %s' % result)

def print_result_cursor(cursor):
    if cursor is None:
        print('No cursor')
    else:
        print('Cursor: %s' % cursor)

def print_result_cursor_list(cursor_list):
    if cursor_list is None:
        print('No cursor list')
    else:
        print('Cursor list: %s' % cursor_list)

def print_result_cursor_list_list(cursor_list_list):
    if cursor_list_list is None:
        print('No cursor list list')
    else:
        print('Cursor list list: %s' % cursor_list_list)

def print_result_cursor_list_list_list(cursor_list_list_list):
   
