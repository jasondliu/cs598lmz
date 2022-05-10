import sys, threading
threading.Thread(target=lambda: sys.stdout.write(unicode('do the thing!\n', 'utf-8'))).start()
</code>
And on Python 2.7.5
<code>$ /usr/local/bin/python2.7 -c \
    "import sys, threading; threading.Thread(target=lambda: sys.stdout.write(u'do the thing!\n')).start()"
do the thing!
$ /usr/local/bin/python2.7 -c \
    "import sys, threading; threading.Thread(target=lambda: sys.stdout.write(unicode('do the thing!\n', 'utf-8'))).start()"
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-11: ordinal not in range(128)
</code>
Of course, this is just a contrived example and I'd always use <code>print u'do the thing!'</code> to write Unicode to stdout if I had a choice, but I'm curious why it works as it does in Python 3.



