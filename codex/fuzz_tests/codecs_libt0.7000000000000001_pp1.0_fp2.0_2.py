import codecs
codecs.open
</code>
Why do I get this error? Is there a way to fix it?


A:

You must use <code>__import__</code> to import a module by name, this should work:
<code>__import__('codecs').open
</code>

