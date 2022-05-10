import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql
pymysql.install_as_MySQLdb()
</code>
But this doesn't work.
I'm using PyCharm to write the code.
I don't know how to solve this problem.
Hope you can help me.

