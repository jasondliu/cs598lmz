fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
'''

if __name__ == '__main__':
    make_unbound_method()
    write_code_object_to_file()
    write_code_object_to_file()
    write_code_object_to_file(None)
    write_code_object_to_file(lambda:None)
    write_code_object_to_file(lambda:None, variables={})
    write_
