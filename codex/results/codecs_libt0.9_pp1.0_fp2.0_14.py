import codecs
codecs.register(Tsf1kReader.search_function)

reader = Tsf1kReader("ccc.tsfr")

for page in reader:
    print page.__dict__
    tmp = pytesseract.image_to_string(page.image)
    print type(tmp)
    if isinstance(tmp, unicode):
        print tmp.encode("utf-8")
    else:
        print tmp
    break
</code>


A:

<code>for x in open("ccc.tsfr"):
    x.decode("utf-16").encode("utf-8")
</code>
Εχει κανει βγει αυτο!

