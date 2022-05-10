import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def write_file(input_file,output_file,input_field,output_field):
    with codecs.open(input_file, 'r', encoding='utf-8', errors='replace_with_space') as f:
        with codecs.open(output_file, 'w', encoding='utf-8') as of:
            for line in f:
                data = line.split("\t")
                if len(data) > 1:
                    of.write(data[input_field]+"\t"+data[output_field]+"\n")

def main(args):
    input_file = args.input_file
    output_file = args.output_file
    input_field = args.input_field
    output_field = args.output_field
    write_file(input_file,output_file,input_field,output_field)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
   
