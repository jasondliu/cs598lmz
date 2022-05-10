fn = lambda: None
gi = (i for i in ())
fn.__code__ = b''
fn2 = types.FunctionType(b'}', {}, '', (), (np.array(1),))
fn3 = lambda a: b'x'
r = fuzzy.PatternException(fn)
r(None)
r = fuzzy.BranchException(fn, fn2)
r(None)
r = fuzzy.Profiler(fn)
del r

fuzzy.trim(b'x')
fuzzy.zeropad(b'x')
fuzzy.spacepad(b'x')
fuzzy.pairs(b'x')
fuzzy.ngrams(b'x', order=1)
fuzzy.parse_doublemetaphone(b'x')
fuzzy.metaphone(b'')
fuzzy.soundex(b'')
fuzzy.match_rating_codex(b'')
fuzzy.match_rating_comparison(b'', b'')
fuzzy.match_rating_codex_norm(b'')
fuzzy.match_rating_comparison
