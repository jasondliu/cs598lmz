fn = lambda: None
# Test fn.__code__.co_filename
if __name__ == '__main__':
    fn.__code__.co_filename == 'test_co_filename.py'

# Test fn.__code__.co_name
if __name__ == '__main__':
    fn.__code__.co_name == '<lambda>'
