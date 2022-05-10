import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_iter_lines(unittest.TestCase):

    def test_iter_lines(self):
        # test iter_lines
        for mode in ['r', 'rb']:
            f = open(test_support.TESTFN, mode)
            try:
                lines = list(f.xreadlines())
            finally:
                f.close()

            f = open(test_support.TESTFN, mode)
            try:
                lines2 = list(f.iter_lines())
            finally:
                f.close()

            self.assertEqual(lines, lines2)

        # test iter_lines with size argument
        for mode in ['r', 'rb']:
            f = open(test_support.TESTFN, mode)
            try:
                lines = list(f.xreadlines())
            finally:
                f.close()

            f = open(test_support.TESTFN, mode)
            try:
                lines2 = list(f.iter_lines(sizehint=
