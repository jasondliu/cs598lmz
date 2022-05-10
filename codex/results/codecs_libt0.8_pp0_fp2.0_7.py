import codecs
codecs.register(my_search)
</code>
Since this is only needed to support the <code>u'\uXXXX'</code> notation and not other unicode escapes, we can check for this notation and only then run our own decoder:
<code>def my_search(encoding):
    if encoding != "unicode-escape":
        return None

    def my_decoder(input, errors='strict'):
        match = re.match(r"u'(?P&lt;data&gt;[^']+)'", input.replace("\\", ""))
        if match is not None:
            data = match.group("data")
            data = data.decode("iso-8859-1")
            return data.encode("utf-8"), len(input)

        return (u'', 0)

    return codecs.CodecInfo(
        name='unicode-escape',
        encode=codecs.unicode_escape_encode,
        decode=my_decoder,
    )


import codecs
codecs.register(my_search
