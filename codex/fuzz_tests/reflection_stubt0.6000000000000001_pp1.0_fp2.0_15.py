fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class TestCsv(unittest.TestCase):
    def test_csv_reader(self):
        with self.assertRaises(TypeError):
            csv.reader(1)
        with self.assertRaises(TypeError):
            csv.reader(fn)
        with self.assertRaises(TypeError):
            csv.reader(gi)

    def test_csv_writer(self):
        with self.assertRaises(TypeError):
            csv.writer(1)
        with self.assertRaises(TypeError):
            csv.writer(fn)
        with self.assertRaises(TypeError):
            csv.writer(gi)

    def test_csv_DictReader(self):
        with self.assertRaises(TypeError):
            csv.DictReader(1)
        with self.assertRaises(TypeError):
            csv.DictReader(fn)
        with self.assertRaises(TypeError):
            csv.DictReader(gi)

    def test_csv_Dict
