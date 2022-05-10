import codecs
codecs.register_error("strict", codecs.ignore_errors)
codecs.register_error("replace", codecs.replace_errors)

import settings

def decode(bytes):
    return codecs.decode(bytes, "utf-8", "replace")

def encode(text):
    return codecs.encode(text, "utf-8")

def get_available_languages():
    try:
        doc = yattag.Doc()
        with doc.tag('ul', id='languages'):
            for lang in settings.Language.list_available_languages():
                with doc.tag('li'):
                    doc.text(lang)
        return doc.getvalue()
    except Exception as e:
        utils.log_error(e)
        return ''


def get_language_forms(lang):
    try:
        doc = yattag.Doc()
        with doc.tag('ul', id='languages'):
            for form in settings.Language.list_available_language_forms(lang):
                with doc.tag('li'):
                   
