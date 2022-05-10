import mmap

def main(argv):
    if len(argv) != 3:
        print('Usage: python3', argv[0], '[input.py] [output.html]')
        return 1

    input_fname = argv[1]
    output_fname = argv[2]

    with open(input_fname, 'r') as input_file:
        with open(output_fname, 'w') as output_file:
            generate_html(input_file, output_file)

    return 0

def generate_html(input_file, output_file):
    print_header(input_file, output_file)
    print_body(input_file, output_file)
    print_footer(output_file)

# prints the html header
def print_header(input_file, output_file):
    print('<!DOCTYPE html>', file=output_file)
    print('<html>', file=output_file)
    print('<head>', file=output_file)
