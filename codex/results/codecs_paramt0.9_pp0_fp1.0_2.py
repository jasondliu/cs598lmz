import codecs
codecs.register_error('surrogate_or_unknown', surrogatepass)

def untransliterate(source_string, unknown='?', replace=False, keep_original=False):
    source_string = source_string.strip()
    transcoder = Transliterator_IT.getInstance()
    utrans = transcoder.transliterate(source_string)#.encode('utf-8').decode('utf-8', 'surrogate_or_unknown')
    if keep_original:
        return utrans, source_string
    else:
        return utrans

def check_translit(source_string, unknown='?', replace=True):
    source_string = source_string.strip()
    transcoder = Transliterator_IT.getInstance()
   # utrans = transcoder.transliterate(source_string.encode('utf-8')).decode('utf-8', 'surrogate_or_unknown')
    utrans = transcoder.transliterate(source_string)#.encode('utf-8').decode('utf-8', 'surrogate_or_
