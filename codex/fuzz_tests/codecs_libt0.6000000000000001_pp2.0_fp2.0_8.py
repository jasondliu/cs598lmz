import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
</code>

