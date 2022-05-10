import codecs
codecs.register_error("replace_with_space", lambda e: (u" " * e.end), "replace_with_space")

f = codecs.open("/Users/kyhong/Desktop/test.txt", "r", "utf-8", "replace_with_space")
</code>

