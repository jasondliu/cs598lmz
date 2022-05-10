import _struct
# Test _struct.Struct.from_param()
from _testcapi import getargs_keywords_only
from _testcapi import getargs_keywords_only_mapping
from _testcapi import getargs_keywords_only_star
from _testcapi import getargs_keywords_only_star_mapping
from _testcapi import getargs_keywords_only_star_star
from _testcapi import getargs_keywords_only_star_star_mapping

# Test keyword-only arguments
def test_keyword_only(self):
    self.assertEqual(getargs_keywords_only(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                     (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    self.assertEqual(getargs_keywords_only(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                           a=1, b=2, c=3, d=4, e=5, f=6,
                                          
