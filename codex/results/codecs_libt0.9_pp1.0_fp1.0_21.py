import codecs
codecs.BOM_UTF8

def read_input(file, is_binary=False):

    if is_binary:
        f = open(file, 'rb')
        return f.read()
    else:
        contents = ""
        with codecs.open(file, encoding='utf-8-sig') as f:
            contents = f.read()
        return contents


def write_output(file, contents):
    f = open(file, 'w', encoding='utf-8')
    f.write(str(contents))
    f.close()


if __name__ == "__main__":
    
    home = os.environ['HOME']
    # train_dir = home + "/data/bytenet/summarization/sumdata/train"
    # test_dir = home + "/data/bytenet/summarization/sumdata/test"
    # eval_dir = home + "/data/bytenet/summarization/sumdata/eval"
    source_file = home + "/data/bytenet/summarization/source"
