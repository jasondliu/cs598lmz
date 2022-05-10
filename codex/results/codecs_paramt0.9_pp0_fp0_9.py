import codecs
codecs.register_error('replace_str', replace_str)
</code>
And use this in <code>read</code>
<code>        with codecs.open(path, 'r', encoding='UTF-8', errors='replace_str') as f:
            output.append(f.read())
</code>
This is the expected output
<code>['this is a test�\ntest�\ntest\n']
</code>

