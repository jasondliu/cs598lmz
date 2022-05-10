import codecs
codecs.register_error('strict', codecs.ignore_errors)
file=codecs.open('c:/windows/system32/drivers/etc/hosts', encoding='cp1252')
for line in file:
    print line.encode('utf-8')
</code>
or replace the <code>cp1252</code> with any encoding you want, or even <code>utf-8</code>.

