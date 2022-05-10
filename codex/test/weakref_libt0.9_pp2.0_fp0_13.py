import weakref

pywikibot.output('Bulbapedia has been turned off for now. Please use the command '
                 '"python pwb.py wikicup".')
if 'wikicup' not in sys.argv:
    sys.exit(0)

_logger = 'wikicup'
ROUNDS = [
    'Round 1',
    'Round 2',
    'Round of 32',
    'Round of 16',
    'Quarterfinals',
    'Semifinals',
    'Final',
    ]

