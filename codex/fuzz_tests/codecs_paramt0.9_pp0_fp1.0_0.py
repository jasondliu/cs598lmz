import codecs
codecs.register_error("sql_strict", codecs.sql_strict)
codecs.register_error("ignore", codecs.ignore_errors)

def main():
    args = sys.argv
    input_path = args[1]
    output_path = args[2]
    with codecs.open(input_path, encoding='raw_unicode_escape',errors='sql_strict') as f:
        with codecs.open(output_path, 'w',encoding='utf-8') as g:
            for lin in f:
                line = lin.encode('raw_unicode_escape').decode('utf-8')
                #print(line)
                try:
                    sub_str = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "\n"
                    g.write(sub_str)
                except UnicodeEncodeError as e:
                    print(line)
                    print(sub_str)
                    print(e)
