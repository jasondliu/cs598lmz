fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
    """
    test_func = self.parse_and_analyze(snippet, __name__)
    graphs = self.infer(test_func, __name__).graphs
    self.assertEqual(graphs['fn'].values(), set())
    self.assertEqual(graphs['fn'].keys(),
                     set([QualifiedName('__main__.fn', 'fn')]))
    self.assertEqual(graphs[graphs['fn']].values(), set())
    self.assertEqual(graphs[graphs['fn']].keys(),
                     set([QualifiedName('__main__.fn', 'fn')]))
    self.assertEqual(graphs[graphs[graphs['fn']]].values(),
                     set([QualifiedName('types.NoneType', 'NoneType')]))

  def test_func_code_set(self):
    snippet = """
def fn():
  code = lambda: None
  code.__code__ = code
    """
    test_func = self.parse
