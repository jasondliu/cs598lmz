import codecs
codecs.register_error('ignore_invalid_codepoints', lambda x: '?')

# "subtitles" is a list of tuples (start, end, text).
subtitles = []

def parse_subtitles(subtitle_file, encoding):
    """ Parse a subtitle file into a list of tuples (start, end, text). """
    for line in subtitle_file:
        if line.startswith('[Events]'):
            break

    for line in subtitle_file:
        if line.strip() == '':
            # Blank line.
            continue

        # Read the first two fields.
        fields = line.split(',', 2)
        if len(fields) < 3:
            # Not a subtitle.
            continue

        # The last field is the subtitle text, which may be quoted.
        text = fields[2].strip()
        if text.startswith('"'):
            text = text[1:]
        if text.endswith('"'):
            text = text[:-1]

        # Add the subtitle to the list.
        subtitles.append
