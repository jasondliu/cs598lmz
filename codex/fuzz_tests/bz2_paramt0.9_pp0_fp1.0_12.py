from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(input_file.read())

input_file.close()

os.remove("input.bz2")

input_file = open("input.html", "r")
encoding = "utf-8"
decode = input_file.read().replace(" ", " ")
html_regex_url = re.compile(r"http[s]?[^(\"|\')]+[\.](png|ico|gif|jpg)")
html_regex = re.compile(r"<[^>]*>")

lesson_nums = []
lesson_names = []
lesson_urls = []

for line in decode.split("\n"):
    if "lesson" in line:
        lesson_urls.append(re.findall(html_regex_url, line))
        for i in line.split("<td")[1:]:
            lesson_nums.append(re.findall(r"\d+", i)[0])
            lesson_names.append(re.findall(
