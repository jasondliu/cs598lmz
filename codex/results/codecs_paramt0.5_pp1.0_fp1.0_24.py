import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Use the codecs module to open the file with UTF-8 encoding
with codecs.open(input_file, 'r', 'utf-8') as f:
    for line in f:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Split the line into fields
        fields = line.split('\t')
        # Assign the fields to variables
        node_id, name, url = fields
        # Generate the output
        output = u'{} {} {}\n'.format(node_id, name, url)
        # Use the codecs module to write the output to the output file
        with codecs.open(output_file, 'a', 'utf-8') as fo:
            fo.write(output)

# Use the codecs module to open the file with UTF-8 encoding
with codecs.open(input_file, 'r', 'utf-8') as f:
    for line in f:
        # Remove leading and trailing whitespace
        line = line.strip()
        #
