import codecs
codecs.register_error('replace_with_space',
                      lambda e: (u' ', e.start + 1))

def translate(text, lang_from, lang_to,
              translator=None, tm=None,
              langpair=(None, None)):
    """
    Translate a string from one language to another.
    """
    if translator is None:
        translator = Translator()
    if tm is None:
        tm = TranslationMemory()

    # If we are translating from the same language we are translating to,
    # do not translate but simply return the input text.
    if lang_from == lang_to:
        return text

    # If no language pair has been specified, simply translate the file
    # using the Google Translate API.
    if langpair[0] is None or langpair[1] is None:
        try:
            translation = translator.translate(text, lang_from, lang_to)
            translated_text = translation['translatedText']
        except Exception:
            print "Exception in translate()"
            translated_text = text
        return translated_text
