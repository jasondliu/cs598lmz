import codecs
codecs.register_error('replace_space',
                      lambda e: (u'\u2424', e.start + 1))

import requests


def read_tags(tag_file):
    """ Read file with tags and parse tag-preferences pairs. """
    tags = {}
    with open(tag_file, encoding='utf') as f:
        for line in f:
            line = line.strip()
            tag, pref = line.split(',')
            if tag in tags:
                if int(pref) > int(tags[tag]):
                    tags[tag] = pref
            else:
                tags[tag] = pref
    return tags


def add_new_tags(original_tags, new_tags):
    """ Add new tags to old tags. """
    for tag, pref in new_tags.items():
        if tag in original_tags:
            if int(pref) > int(original_tags[tag]):
                original_tags[tag] = pref
        else:
            original_tags[tag] = pref
    return original_tags


def read_url(
