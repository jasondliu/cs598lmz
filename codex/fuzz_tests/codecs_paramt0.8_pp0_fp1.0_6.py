import codecs
codecs.register_error('my_strict', codecs.strict_errors)

def test_strict(input_fname, encoding):
    with codecs.open(input_fname,
                     mode='rU',
                     encoding=encoding,
                     errors='my_strict',
                     ) as f:
        for line in f:
            # print(line, end="")
            pass


if __name__ == "__main__":

    # input_file = "./my_data/my_bad_utf8.txt"

    # test_strict(input_file, 'iso-8859-1')
    # test_strict(input_file, 'utf-8')
    # test_strict(input_file, 'utf-16')


    input_file = "./my_data/my_good_utf8.txt"
    test_strict(input_file, 'utf-8')
