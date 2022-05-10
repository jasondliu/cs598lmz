import codecs
codecs.getreader("utf-8")(sys.stdin).read()
</code>
which tells Python to try its best to read the text in UTF-8, but if that fails, fall back to the user's locale.

