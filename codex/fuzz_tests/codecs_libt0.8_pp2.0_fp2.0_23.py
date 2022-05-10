import codecs
codecs.register(lambda encoding: codecs.lookup('utf-8') if encoding == 'cp65001' else None)

# Workaround for JS, or else it will be executed
import re
def escape_for_js(s):
    return re.sub(r'(?<=[^\\])\'', r'\\\'', s)

# Get some static data from the database
db = Mysqldb()
db.connect()
s = db.select('select * from metas where type = "category" order by content,id')
db.close()
category_list = '\n'.join(['<li id="category-{0}"><span>{1}</span><span class="hide">|{2}</span></li>'.format(category['id'], escape_for_js(category['content']), category['id']) for category in s])
s = db.select('select * from metas where type = "status" order by content,id')
db.close()
status_list = '\n'.join(['<li id="status-{0}
