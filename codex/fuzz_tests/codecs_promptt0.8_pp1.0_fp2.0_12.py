import codecs
# Test codecs.register_error
import test.test_codecs_charmap
import test.test_codecs_cn
import test.test_codecs_hk
import test.test_codecs_jp
import test.test_codecs_kr
import test.test_codecs_tw

# Test encodings
test.test_codecs_charmap.test_main()
test.test_codecs_cn.test_main()
test.test_codecs_hk.test_main()
test.test_codecs_jp.test_main()
test.test_codecs_kr.test_main()
test.test_codecs_tw.test_main()

# Test that the C codecs don't segfault ##################
import test.test_codecs
test.test_codecs.test_main()

import io
# Test file format detection
test.test_codecs.test_open(io.open, io.TextIOWrapper)

# Test that the UTF-7 codecs
