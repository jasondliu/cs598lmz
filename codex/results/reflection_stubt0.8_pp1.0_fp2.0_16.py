fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class TestParse(unittest.TestCase):
    def test_basic(self):
        node = parse(
            '''
        # comment
        val = "value"
        '''
        )
        self.assertEqual(str(node), 'val = "value"')

    def test_comment(self):
        node = parse(
            '''
        # comment
        '''
        )
        self.assertEqual(str(node), '# comment')

    def test_oneline(self):
        node = parse('val = "value"')
        self.assertEqual(str(node), 'val = "value"')

    def test_number(self):
        node = parse('var = 1')
        self.assertEqual(str(node), 'var = 1')

    def test_asall(self):
        node = parse('var = *1')
        self.assertEqual(str(node), 'var = *1')

    def test_list(self):
        node = parse('var = [1, 2
