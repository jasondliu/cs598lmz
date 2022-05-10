fn = lambda: None
# Test fn.__code__ == None
- assert fn.__code__ is None
# Test fn.__code__.co_filename returns correct file name
- assert fn.__code__.co_filename == os.path.realpath(__file__)
- assert fn.__code__.co_name == '<lambda>'
- assert fn.__name__ == '<lambda>'
# Test fn.__module__ returns correct module name
- assert fn.__module__ == os.path.splitext(os.path.basename(__file__))[0]

fn.__name__ = 'myfunc'
# Test fn.__code__ == None
- assert fn.__code__ is None
- assert fn.__code__.co_filename == os.path.realpath(__file__)
- assert fn.__code__.co_name == 'myfunc'
- assert fn.__name__ == 'myfunc'
# Test fn.__module__ returns correct module name
- assert fn.__module__ == os.path.splitext(os.path.basename(__file__))[0
