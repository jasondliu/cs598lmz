import codecs
# Test codecs.register_error
with codecs.open(filename, "rb", encoding="utf-8", errors="replace") as f:
    print(f.read())
</code>
This results in:
<code>Its model\nnumber is N7100.
</code>
Unfortunately this is just a workaround, since it obviously removes the "untranslated" character that makes the <code>ascii</code> decoding error.

