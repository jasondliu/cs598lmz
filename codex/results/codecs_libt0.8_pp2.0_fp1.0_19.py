import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def build_script(input_file, output_file, palette_file, extra_palette_file=None):
    input = open(input_file, 'r')
    output = open(output_file, 'w')
    
    for line in input:
        if line[:6] == 'Palette':
            output.write('#define ' + line[:-1] + '\n')
            output.write('#include \"' + palette_file + '\"\n')
            if extra_palette_file:
                output.write('#include \"' + extra_palette_file + '\"\n')
        elif line[:7] == '#define':
            output.write(line)
        elif len(line.strip()) > 0 and line.strip()[0] != '#':
            output.write('//' + line)
            
    input.close()
    output.close()
    
def main():
    parser
