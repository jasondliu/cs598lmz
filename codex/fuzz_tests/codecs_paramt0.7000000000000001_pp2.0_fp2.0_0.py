import codecs
codecs.register_error("strict", codecs.strict_errors)
codecs.register_error("surrogateescape", codecs.surrogateescape_errors)
codecs.register_error("replace", codecs.replace_errors)

# for i in range(0, len(encoding_list)):
#     try:
#         codecs.lookup(encoding_list[i])
#         print("{} is supported".format(encoding_list[i]))
#     except LookupError as e:
#         print("{} is not supported".format(encoding_list[i]))

# f = open("../files/utf-8.txt", "w", encoding="utf-8")
# f.write("한글")
# f.close()
#
# f = open("../files/utf-8.txt", "r", encoding="utf-8")
# print(f.read())

# f = open("../files/utf-8.txt", "r", encoding="utf-8")
# print(f.read())
#
