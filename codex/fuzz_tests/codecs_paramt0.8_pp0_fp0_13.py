import codecs
codecs.register_error('error_handler', error_handler)

# Open the file for reading
with open('log.txt', 'r', encoding='utf-8', errors='error_handler') as f:
    print(f.read())

# Create list of non-ASCII characters
non_ascii_list = []
for character in range(0, 256):
    if character != ord('\n') and character != ord('\t') and character != ord('\r') and character != ord('\x0b') and character != ord('\x0c'):
        if chr(character) not in string.printable:
            non_ascii_list.append(character)

print('Non-ASCII characters:')
for char in non_ascii_list:
    print(char, chr(char))

# Prepare the file for writing
infile = codecs.open('log.txt', 'r', encoding='utf-8') # Open the file for reading
outfile = codecs.open('outfile.txt', 'w') # Open the file for writing

# For each
