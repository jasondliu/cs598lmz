import codecs
# Test codecs.register_error("my_ignore", MyIgnore)

# Use the codecs module to open the file with the
# my_ignore error handler. The argument 'ignore' tells
# the codecs module to ignore errors, which is
# not recommended.
with codecs.open("t2.txt", "r", encoding="utf-8", errors="replace") as fp:
  while True:
    buf = fp.read(10)
    if not buf:
      break
    print("next 10 characters:", buf, file=sys.stdout)
# next 10 characters: Ḥadīṯ
# next 10 characters:
# next 10 characters: aḥmad b.
# next 10 characters: Ṭalḥa
# next 10 characters: b. Muḥ
# next 10 characters: ammad al-Ṭ
# next 10 characters: arī, Bāb
# next 10 characters: al-ḥadīṯ,
# next 10 characters: ʿAbd al-ʿA
# next 10 characters: zīz b. ʿAl
# next 10
