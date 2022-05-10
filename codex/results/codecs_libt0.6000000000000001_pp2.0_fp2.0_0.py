import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re

# input_file = sys.argv[1]
# input_file = 'test_data.txt'

input_file = 'input.txt'

# input_file = 'input_with_titles.txt'
# input_file = 'input_with_titles_new.txt'

# input_file = 'input_with_titles_all.txt'

# input_file = 'input_with_titles_all_new.txt'

# input_file = 'input_with_titles_all_new_new.txt'

# input_file = 'input_with_titles_all_new_new_new.txt'

# input_file = 'input_with_titles_all_new_new_new_new_new.txt'

# input_file = 'input_with_
