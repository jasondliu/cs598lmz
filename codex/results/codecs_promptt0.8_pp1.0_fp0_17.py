import codecs
# Test codecs.register_error
# http://bugs.python.org/issue7097
codecs.register_error('test.surrogateescape', codecs.backslashreplace_errors)
import pickle
import tempfile

def test_main():
    pickle_file = tempfile.mktemp()
    try:
        pickle.dump(object(), open(pickle_file, 'wb'))
        pickle.load(open(pickle_file, 'rb'))
    finally:
        os.remove(pickle_file)

    pickle_file = tempfile.mktemp()
    try:
        pickle.dump(object(), open(pickle_file, 'wb'))
        pickle.load(open(pickle_file, 'rb'), errors='test.surrogateescape')
    finally:
        os.remove(pickle_file)


if __name__ == "__main__":
    test_main()
