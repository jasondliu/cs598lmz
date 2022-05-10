import mmap

DEFAULT_VARIABLE_PATTERN = re.compile(
    r"""
    \{\{  # Opening double-brace {{
    ([^\}]+)  # Anything but closing brace
    \}\}  # Closing double-brace }}
    """,
    re.UNICODE | re.VERBOSE
)


def _update_template(template, pattern, **kwargs):
    # Use mmap to open the template file and update variables in-place
    with open(template, 'r+b') as template_file:
        template_mmap = mmap.mmap(template_file.fileno(), 0)
        for match in iter(lambda: pattern.search(template_mmap), None):
            key = match.group(1)
            value = kwargs.get(key, '')
            template_mmap[match.start():match.end()] = value
        template_mmap.close()


def update_template(template, **kwargs):
    _update_template(template, DEFAULT_VARIABLE_PAT
