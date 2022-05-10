import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Opens the file of the OCR'd text
#file = open("Texts/WOL_ENG_v1_OCR.txt")
#file = open("Texts/WOL_LAT_v1_OCR.txt")
#file = open("Texts/WOL_ENG_v2_OCR.txt")
#file = open("Texts/WOL_LAT_v2_OCR.txt")
#file = open("Texts/WOL_ENG_v3_OCR.txt")
#file = open("Texts/WOL_LAT_v3_OCR.txt")
#file = open("Texts/WOL_ENG_v4_OCR.txt")
#file = open("Texts/WOL_LAT_v4_OCR.txt")
#file = open("Texts/WOL_ENG_v5_OCR.txt")
#file = open("Texts/WOL_L
