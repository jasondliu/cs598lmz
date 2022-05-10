import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# Set up space replacement
replacements = [(u'\u00a0', u' ')]


def replace_chars(s):
    new_str = s
    for r in replacements:
        new_str = new_str.replace(*r)
    return new_str


def main():
    # Read in the file
    with codecs.open('census-error.html', 'r', encoding='utf8',
                     errors='replace_with_space') as f:
        html = f.read()
    # Replace bad characters with spaces
    html = replace_chars(html)
    # Write the file
    with codecs.open('census-fixed.html', 'w', encoding='utf8') as f:
        f.write(html)


if __name__ == '__main__':
    main()
