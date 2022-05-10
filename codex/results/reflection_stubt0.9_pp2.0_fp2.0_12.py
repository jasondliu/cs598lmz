fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
result = fn.__code__.__next__()
""",
                  "patterns": (
                    (".0'UIException(",
                     (`, `, '.0',
                      '=.1')),
                    (".0'.0'",
                     (`UIException: ', ``,
                      '.1',
                      '=.2')),
                    ("""\
(.2, .0'python: object expected (got generator)',
 .0'<module> (line 4)')""",
                     (`[Exception,
                        [Line, 4, 4],
                        [Column, 21, 27],
                        [BytecodeOffset, 72, 78],
                        [Function, ".0'<module>", 1, 123]],`,
                      `'UIException(`,
                      `.1',
                      ` [Exception,
                        [Line, 1, 1],
                        [Column, 0, 6],
                        [BytecodeOffset, 1, 7],
                        [Function, ".0'<module>", 1, 123]],`,
                      ` [Exception,
                        [Line, 1, 1
