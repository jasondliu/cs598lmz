import lzma
lzma.LZMACompressor(format=lzma.FORMAT_ALONE)

def add_tests(environment):
  test_environment.load_tests(environment)

def main():
  parser = optparse.OptionParser('%prog [options]',
                                 description=__doc__)
  parser.add_option('--outdir', default='.',
                    help='Directory to place results in.')
  parser.add_option('--tarball',
                    help='Tarball that has all test files to use for the test.')
  parser.add_option('--use-emulator',
                    help='Run the emulator for ARM.')
  parser.add_option('--test-only',
                    help='Run tests only, no build.')
  parser.add_option('--build-only',
                    help='Run build only, no tests.')
  parser.add_option('--enable-ccache', default=False,
                    help='Use ccache.')
  parser.add_option('--expectations',
                    help='Override the expectations file.')

