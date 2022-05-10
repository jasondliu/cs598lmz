import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

# Append regular expressions here. The regex is checked against the
# path component of the URI. If a component matches any regex, the
# downloader tries to download the file.
ARCHIVE_REGEX = [
    '^.*\\.tar\\.gz$',
    '^.*\\.tgz$',
    '^.*\\.tar\\.bz2$',
    '^.*\\.7z$',
    '^.*\\.zip$'
]

# Append regular expressions here. The regex uses extended format,
# as described in https://docs.python.org/2/library/re.html#re.X
RE_ARCHIVE_REGEX = [
    r'.*\.tar\.gz$',
    r'.*\.tgz$',
    r'.*\.tar\.bz2$',
    r'.*\.7z$',
    r'.*\.zip$'
]

# Append regular expressions here. The regex is checked against the
# path component of the URI. If a component
