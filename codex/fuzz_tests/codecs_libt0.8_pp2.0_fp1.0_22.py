import codecs
codecs.register_error("strict", codecs.ignore_errors)


class TestCore(unittest.TestCase):

    def test_none(self):
        f = StringIO()
        with PrettyTable(["Field 1", "Field 2"], stream=f) as pt:
            pt.align = "l"
            pt.add_row([None, None])

        self.assertEqual(f.getvalue(), u"+---------+---------+\n| Field 1 | Field 2 |\n+---------+---------+\n|         |         |\n+---------+---------+\n")

    def test_format_none(self):
        f = StringIO()
        with PrettyTable(["Field 1", "Field 2"], stream=f) as pt:
            pt.align = "l"
            pt.add_row([pt.format(None), pt.format(None)])

        self.assertEqual(f.getvalue(), u"+---------+---------+\n| Field 1 | Field 2 |\n+---------+---------+\n|         |         |\n+--------
